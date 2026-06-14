# PDF Merger Tool
A  lightweight Python script that merges multiple PDF files into a single document. 
This script uses the `PyMuPDF` library to handle complex PDFs, annotations and formatting without file corruption.

## Features
- Merges all `.pdf` files in the same directory as the script.
- Alphabetical sorting ensures your files are merged in the exact order you want.
- Safe execution: Automatically ignores previously generated output files to prevent recursive merging.
- Robust processing using PyMuPDF to cleanly handle complex layouts, form fields and annotations.

## Prerequisites
- Python 3.x installed.
- The `PyMuPDF` library.

### Installation of `PyMuPDF`
1. Open your Terminal or Command Prompt.
2. Install the required library by running:
   ```
   pip install pymupdf
   ```

## Usage
1. Create a dedicated folder on your computer.
2. Place the `merge.py` script into this folder.
3. Copy all the PDF files you want to merge into the same folder.
4. Right-click on your folder and click 'Open in Terminal', then run this command:
   ```
   python merge.py
   ```
**Tip:** The script processes files alphabetically. To force a specific order, prefix your file names with numbers (e.g., `01_cover.pdf`, `02_intro.pdf`, `03_report.pdf`).


## Output
The script will generate a new file named `00_mergedpdf.pdf` in the same folder containing all your combined pages.



### Example of folder
PDFMerger/
├── merge.py
├── 01_cover.pdf
├── 02_intro.pdf
└── 03_report.pdf
