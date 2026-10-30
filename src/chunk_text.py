from pathlib import Path

# Locate project folder
project_folder = Path(__file__).resolve().parent.parent

# Locate extracted text file
input_path = project_folder / "data" / "extracted_text.txt"

# Read the extracted text
with open(input_path, "r", encoding="utf-8") as file:
    text = file.read()

# Define chunk size and overlap
chunk_size = 500
overlap = 50

chunks = []

# Divide text into chunks
start = 0

while start < len(text):
    end = start + chunk_size

    chunk = text[start:end]
    chunks.append(chunk)

    start = end - overlap

# Display results
print("Total chunks:", len(chunks))

for i, chunk in enumerate(chunks[:3]):
    print(f"\n--- Chunk {i + 1} ---")
    print(chunk)
