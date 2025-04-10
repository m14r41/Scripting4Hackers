
import os
import pdfplumber
import pandas as pd

def extract_pdf_data(pdf_file):
    # Open the PDF file
    with pdfplumber.open(pdf_file) as pdf:
        text_data = []
        for page in pdf.pages:
            # Extract table (or text) from each page
            table = page.extract_table()
            if table:
                # Append each row from the table
                for row in table:
                    # Clean up empty columns or rows
                    row = [cell.strip() if isinstance(cell, str) else cell for cell in row]
                    text_data.append(row)
        return text_data

def convert_pdf_to_excel(pdf_path, output_filename="output.xlsx"):
    # Extract data from PDF
    data = extract_pdf_data(pdf_path)

    if data:
        # Handle mismatched columns: Ensure all rows have the same number of columns
        max_columns = max(len(row) for row in data)  # Find the maximum number of columns
        for i in range(len(data)):
            while len(data[i]) < max_columns:
                data[i].append('')  # Append empty strings to make the row length consistent

        # Convert to DataFrame, with the first row as headers
        df = pd.DataFrame(data[1:], columns=data[0])  # Use the first row as column names
        df.to_excel(output_filename, index=False, engine='openpyxl')
        print(f"Excel file '{output_filename}' saved in the current folder.")
    else:
        print("No table data found in the PDF file.")

def main():
    # Ask user for the path to the PDF file
    pdf_file = input("Please provide the path to the PDF file: ")

    # Check if the file exists
    if os.path.exists(pdf_file) and pdf_file.lower().endswith('.pdf'):
        # Convert the PDF to Excel and save it in the current directory
        convert_pdf_to_excel(pdf_file)
    else:
        print("The provided file doesn't exist or isn't a PDF file.")

if __name__ == "__main__":
    main()
