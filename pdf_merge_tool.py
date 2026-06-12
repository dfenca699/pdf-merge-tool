from pypdf import PdfWriter
from pathlib import Path


def merge_pdfs(input_files, output_file):
    writer = PdfWriter()

    for file_path in input_files:
        path = Path(file_path)

        if not path.exists():
            print(f"File not found: {file_path}")
            continue

        if path.suffix.lower() != ".pdf":
            print(f"Skipped non-PDF file: {file_path}")
            continue

        writer.append(str(path))

    with open(output_file, "wb") as output:
        writer.write(output)

    print(f"Merged PDF saved to: {output_file}")


if __name__ == "__main__":
    print("PDF Merge Tool")
    print("Enter PDF file paths separated by commas.")
    print("Example: file1.pdf,file2.pdf,file3.pdf")

    files = input("PDF files: ").split(",")
    files = [file.strip() for file in files]

    output = input("Output file name, for example merged.pdf: ").strip()

    if not output.endswith(".pdf"):
        output += ".pdf"

    merge_pdfs(files, output)
