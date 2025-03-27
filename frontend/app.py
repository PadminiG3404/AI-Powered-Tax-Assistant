import streamlit as st
import requests

st.title("AI Tax Assistant")
st.subheader("Upload a Receipt to Analyze Tax Deductions")

uploaded_file = st.file_uploader("Choose a receipt image...", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    files = {"file": uploaded_file.getvalue()}
    response = requests.post("http://localhost:8000/upload-receipt/", files=files)

    if response.status_code == 200:
        st.write("Extracted Text:")
        st.write(response.json()["text"])

        st.write("Potential Tax Deductions:")
        st.write(response.json()["deductions"])
