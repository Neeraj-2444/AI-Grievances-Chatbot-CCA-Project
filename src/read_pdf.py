from pypdf import PdfReader
from pathlib import Path

# Locate the project folder
project_folder = Path(__file__).resolve().parent.parent

# Locate the PDF
pdf_path = project_folder / "data" / "ug_academic_rules_2021_onwards.pdf"

# Open the PDF
reader = PdfReader(pdf_path)

print("Total pages:", len(reader.pages))

# Store extracted text
all_text = ""

# Extract text from ALL pages
for page_number, page in enumerate(reader.pages):
    text = page.extract_text()

    if text:
        all_text += f"\n--- Page {page_number + 1} ---\n"
        all_text += text

# Save extracted text
output_path = project_folder / "data" / "extracted_text.txt"

with open(output_path, "w", encoding="utf-8") as file:
    file.write(all_text)

print("Text extraction completed!")
print("Saved to:", output_path)

