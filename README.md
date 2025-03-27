# 🚀 TaxMate: AI-Powered Tax Assistant

## 📌 Overview

**Amplifying Human Potential Using AI** - TaxMate is a smart, AI-powered tax assistant designed to automate the tax filing process. It simplifies complex calculations, identifies deductions, and minimizes errors, making tax filing more efficient and accessible for individuals and businesses.

<p align="center">
    <img width="400" src="https://github.com/user-attachments/assets/0881158f-dc0d-4f08-9d46-ba072d1f0227">

--- 

## 🌟 Features
- **Automated Tax Calculation** - Rule-based engine for accurate tax computation.  
- **AI-Powered Query Assistant** - NLP-based chatbot for tax-related queries.  
- **OCR for Document Parsing** - Extracts income details from tax forms, salary slips, and invoices.  
- **Error Detection & Deduction Identification** - AI-driven insights to minimize errors and optimize tax benefits.  
- **Secure & Compliant** - Data encryption, OAuth2 authentication, and compliance with tax regulations.  

---

## 🏗️ Tech Stack

| Component          | Technologies Used |
|-------------------|------------------|
| **Programming Language** | Python |
| **Backend** | Flask, FastAPI |
| **Frontend** | Flask (UI) |
| **Database** | SQLite |
| **AI/ML** | Tesseract OCR, OpenAI API, Regex-based Extraction |
| **Security** | OAuth2, AES Encryption |
| **Deployment** | Docker, AWS |

---
## 📂 Project Structure

```
📁 TaxMate
│── 📄 README.md
│── 📁 backend
│   │── __init__.py
│   │── models/
│   │   │── database.py  # Database configurations
│   │   │── main.py  # Core processing logic
│   │   │── receipt_ocr.log  # OCR processing logs
│   │   │── tax_data.db  # Tax-related stored data
│   │   │── temp_receipt4.png  # Sample test image for OCR
│   │   ├── __pycache__/  # Compiled Python files
│── 📁 frontend
│   │── app.py  # Main frontend script
```

---
## ⚡ Installation & Setup

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/yourusername/taxmate.git
cd taxmate
```

### 2️⃣ Install Dependencies
#### Backend
```sh
cd backend
pip install -r requirements.txt
```
#### Frontend
```sh
cd frontend
pip install flask
```

### 3️⃣ Run the Application
#### Start Backend (FastAPI)
```sh
cd backend
uvicorn app:app --reload
```
#### Start Frontend (React.js)
```sh
cd frontend
npm run dev
```

### 4️⃣ Access the App
Open **`http://localhost:3000`** in your browser.

---
## 🎯 API Endpoints  

| Endpoint         | Method | Description                            |
|-----------------|--------|----------------------------------------|
| `/extract-text` | POST   | Extracts text from uploaded invoice   |
| `/calculate-tax` | POST   | Computes tax based on user inputs     |
| `/get-deductions` | GET   | Returns AI-suggested deductions      |
| `/validate-tax`  | POST   | Checks for errors in tax filing      |

---
## 🚀 Deployment
### Using Docker:
```sh
docker-compose up --build
```

---
## 🛡️ Security & Compliance
- **AES-256 Encryption** for sensitive data.
- **OAuth2 Authentication** (Google/Microsoft Login).
- **Audit Logs** to track changes.

---
## 📬 Contact
For queries, reach out at: **pgudavalli2004@gmail.com**  
