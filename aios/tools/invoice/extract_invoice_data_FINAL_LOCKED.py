# -*- Standards Compliance Declaration -*-
# File: extract_invoice_data.py
# Purpose: Extract metadata from scanned or digital invoices for AIOS accounting ingestion
# Standards:
#   - ISO/IEC 27001 (Data Security)
#   - ISO/IEC 12207 (Software Lifecycle)
#   - IRS Publication 1075 (Document confidentiality)
#   - ABL_Rev2_6_1_25 (Internal compliance standards)
# Owner: Adaptive Bespoke Learning – AI Tools Team
# Last Updated: 2025-06-02

"""
This script is FINAL_LOCKED unless reopened by system administrator.
It uses OCR to extract invoice fields from PDFs or scanned images and prepares them
for AIOS ingestion into financial workflows or grant accounting review.
"""

import pytesseract
from PIL import Image
import re
import os

def extract_invoice_metadata(image_path):
    if not os.path.exists(image_path):
        raise FileNotFoundError("Invoice image not found.")

    text = pytesseract.image_to_string(Image.open(image_path))
    metadata = {}

    # Simple patterns for MVP extraction
    date_match = re.search(r"(Date|DATE|date)[\s:]*([\d/.-]+)", text)
    vendor_match = re.search(r"(From|Vendor|Billed by)[\s:]*([\w\s,.-]+)", text)
    amount_match = re.search(r"\$?(\d{1,3}(?:[.,]\d{3})*(?:[.,]\d{2}))", text)

    if date_match:
        metadata["date"] = date_match.group(2).strip()
    if vendor_match:
        metadata["vendor"] = vendor_match.group(2).strip()
    if amount_match:
        metadata["amount"] = amount_match.group(1).replace(",", "").strip()

    return metadata

# Example usage
if __name__ == "__main__":
    sample_path = "sample_invoice.jpg"  # Replace with real input path
    try:
        result = extract_invoice_metadata(sample_path)
        print("Extracted Invoice Data:")
        print(result)
    except Exception as e:
        print("Error:", e)
