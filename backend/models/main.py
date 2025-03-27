import os
import re
import cv2
import shutil
import logging
import numpy as np
import pytesseract
from PIL import Image
from fastapi import FastAPI, File, UploadFile
from fuzzywuzzy import process

# Configure logging
logging.basicConfig(filename="receipt_ocr.log", level=logging.DEBUG, format="%(asctime)s - %(message)s")

app = FastAPI()

# Set Tesseract OCR Path (modify if needed)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Function to resize large images
def resize_image(image_path):
    """Resize large images to a fixed width while maintaining aspect ratio."""
    img = cv2.imread(image_path)
    height, width = img.shape[:2]

    if width > 1000:  # Resize only if the image is too large
        scale_ratio = 1000 / width
        new_height = int(height * scale_ratio)
        img = cv2.resize(img, (1000, new_height), interpolation=cv2.INTER_AREA)
    
    return img

# Function to preprocess images for better OCR accuracy
def preprocess_image(image_path):
    """Preprocess image for improved OCR results."""
    image = resize_image(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    processed_img = cv2.adaptiveThreshold(
        blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
    )
    kernel = np.ones((1, 1), np.uint8)
    processed_img = cv2.morphologyEx(processed_img, cv2.MORPH_CLOSE, kernel)
    return processed_img

# Function to extract text using OCR
def extract_text(image_path):
    """Extract text from an image using Tesseract OCR with improved settings."""
    processed_img = preprocess_image(image_path)

    # OCR settings: Use psm 6 (single block text), with a character whitelist
    custom_config = r'--psm 6 -c tessedit_char_whitelist="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789$%.,:-"'
    
    extracted_text = pytesseract.image_to_string(processed_img, config=custom_config)
    return extracted_text

# Function to extract tax details using fuzzy matching
def extract_tax_details(ocr_text):
    """Extract total amount, tax percentage, and tax amount from OCR text using fuzzy matching."""
    total_keywords = ["Total", "Grand Total", "Amount Due", "Balance Due"]
    tax_keywords = ["Sales Tax", "VAT", "GST", "Tax Rate", "Service Tax"]

    total_pattern = r"\$?([\d,]+\.\d{2})"
    
    # Find best match for total
    total_line = None
    for line in ocr_text.split("\n"):
        match, score = process.extractOne(line, total_keywords)
        if score > 80:  # Adjust threshold as needed
            total_line = line
            break

    # Extract total amount
    total_match = re.search(total_pattern, total_line) if total_line else None
    total_amount = float(total_match.group(1).replace(",", "")) if total_match else None

    # Find best match for tax
    tax_line = None
    for line in ocr_text.split("\n"):
        match, score = process.extractOne(line, tax_keywords)
        if score > 80:
            tax_line = line
            break

    # Extract tax percentage and amount
    tax_pattern = r"([\d.]+)%?\s*\$?([\d,]+\.\d{2})?"
    tax_match = re.search(tax_pattern, tax_line) if tax_line else None

    tax_percentage = float(tax_match.group(1)) if tax_match and tax_match.group(1) else None
    tax_amount = float(tax_match.group(2).replace(",", "")) if tax_match and tax_match.group(2) else None

    return {
        "total_amount": total_amount,
        "tax_percentage": tax_percentage,
        "tax_amount": tax_amount,
    }

@app.post("/upload/")
async def upload_receipt(file: UploadFile = File(...)):
    """API endpoint to upload and process receipts."""
    file_location = f"./temp_{file.filename}"

    # Save the uploaded file
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract text using OCR
    extracted_text = extract_text(file_location)

    # Log OCR output for debugging
    logging.debug(f"OCR Extracted Text for {file.filename}:\n{extracted_text}\n")

    # Extract tax details
    tax_info = extract_tax_details(extracted_text)

    # Cleanup: Remove the temporary image file
    os.remove(file_location)

    return {
        "filename": file.filename,
        "extracted_text": extracted_text,
        "tax_info": tax_info
    }
