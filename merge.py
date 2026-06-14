import os
import fitz  # PyMuPDF

def merge_pdfs_in_folder(folder_path, output_filename="00_mergedpdf.pdf"):
    # Find all PDFs and sort them to make sure we ignore any old corrupted output
    pdf_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.pdf') and f != output_filename]
    pdf_files.sort()

    if not pdf_files:
        print("No PDF files found in this folder.")
        return

    print(f"Found {len(pdf_files)} PDFs. Merging now...\n")

    # Create a blank PDF to hold everything
    merged_pdf = fitz.open()

    for pdf in pdf_files:
        file_path = os.path.join(folder_path, pdf)
        try:
            # Open the individual PDF and insert it into our merged document
            with fitz.open(file_path) as doc:
                merged_pdf.insert_pdf(doc)
            print(f"Added: {pdf}")
        except Exception as e:
            print(f"Failed to add {pdf}. Error: {e}")

    # Save the final document
    output_path = os.path.join(folder_path, output_filename)
    merged_pdf.save(output_path)
    merged_pdf.close()
    
    print(f"\nYour fully combined file is saved as: {output_filename}")

if __name__ == "__main__":
    current_folder = os.getcwd()
    merge_pdfs_in_folder(current_folder)
