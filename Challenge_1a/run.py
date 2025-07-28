import os
import sys
from process import extract_outline, save_outline

INPUT_DIR = "input"
OUTPUT_DIR = "output"

os.makedirs(OUTPUT_DIR, exist_ok=True)

pdf_files = [f for f in os.listdir(INPUT_DIR) if f.lower().endswith(".pdf")]

if not pdf_files:
    print("❌ No PDF files found in input folder.")
    sys.exit(1)

for pdf in pdf_files:
    pdf_path = os.path.join(INPUT_DIR, pdf)
    print(f"📄 Processing: {pdf}")
    result = extract_outline(pdf_path)
    save_outline(pdf_path, result)

print("✅ All PDFs processed.")
