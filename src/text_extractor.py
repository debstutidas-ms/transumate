import pdfplumber


def extract_text_from_pdf(pdf_path):
    text = ""

    # Open the PDF file
    with pdfplumber.open(pdf_path) as pdf:
        # Iterate through each page
        for page in pdf.pages:
            text += page.extract_text()  # Extract text from the page

    return text


# Example usage
pdf_file_path = '/Users/debstutidas/Documents/MLProjects/translation_gpt/chinese_simple.pdf'
extracted_text = extract_text_from_pdf(pdf_file_path)
print(extracted_text)
