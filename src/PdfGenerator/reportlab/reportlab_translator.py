import os
from pathlib import Path
from PyPDF2 import PdfMerger
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics


local_languages = {
    'Bengali': ('BengaliFont', 'NotoSansBengali-VariableFont_wdth,wght.ttf'),
    'Hindi': ('HindiFont', 'NotoSansDevanagari-VariableFont_wdth,wght.ttf'),
    'Kannada': ('KannadaFont', 'NotoSansKannada-VariableFont_wdth,wght.ttf'),
    'Tamil': ('TamilFont', 'NotoSansTamil-VariableFont_wdth,wght.ttf'),
    'Malayalam': ('', ''),
    'Chinese Simple': ('ChineseFont', 'NotoSansSC-VariableFont_wght.ttf'),
    'Chinese Traditional': ('ChineseFont', 'NotoSansTC-VariableFont_wght.ttf'),
    'Japanese': ('JapaneseFont', 'NotoSansJP-VariableFont_wght.ttf')
}


def create_pdf(input_txt_file, output_pdf_file, language):
    # Create a PDF canvas
    c = canvas.Canvas(output_pdf_file, pagesize=letter)

    font = 'Helvetica'

    if language in local_languages:
        # Register the Bengali font
        font, ttf = local_languages[language][0], local_languages[language][1]
        pdfmetrics.registerFont(TTFont(font, ttf))

    c.setFont(font, 11)

        # Read the Bengali text from the input file
    with open(input_txt_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

        # Define margins
        TOP_MARGIN = 50
        BOTTOM_MARGIN = 50
        LEFT_MARGIN = 50
        RIGHT_MARGIN = 50

        # Calculate the usable height and starting y position
        usable_height = letter[1] - TOP_MARGIN - BOTTOM_MARGIN
        y_position = letter[1] - TOP_MARGIN

        # Calculate the usable width
        usable_width = letter[0] - LEFT_MARGIN - RIGHT_MARGIN

        # Read the Bengali text from the input file
        with open(input_txt_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()

            # Write each line of the text to the PDF
            for line in lines:
                # Ensure the line fits within the usable width
                if len(line.strip()) > 0:
                    # Draw the string and check if it goes beyond the right margin
                    text_width = c.stringWidth(line.strip(), font, 12)
                    if text_width > usable_width:
                        # Split the line into smaller parts if it exceeds the right margin
                        words = line.strip().split()
                        current_line = ""
                        for word in words:
                            test_line = current_line + word + " "
                            if c.stringWidth(test_line, font, 12) > usable_width:
                                c.drawString(LEFT_MARGIN, y_position, current_line)
                                y_position -= 15  # Move down for the next line
                                current_line = word + " "
                            else:
                                current_line = test_line
                        if current_line:
                            c.drawString(LEFT_MARGIN, y_position, current_line)
                            y_position -= 15  # Move down after the last line

                # Check if we need to create a new page
                if y_position < BOTTOM_MARGIN:  # If near the bottom of the page
                    c.showPage()  # Create a new page
                    c.setFont('BengaliFont', 12)
                    y_position = letter[1] - TOP_MARGIN  # Reset y position for the new page

            # Finalize the PDF
            c.save()


# if __name__ == "__main__":
#     input_file = '/Users/debstutidas/Documents/MLProjects/transumate/src/Samples/TXT/english.txt'
#     file_name = 'english.pdf'
#
#     output_base_dir = '/Users/debstutidas/Documents/MLProjects/transumate/src/Samples/PDF'
#     # Path(os.path.join(output_base_dir, 'bengali.pdf')).mkdir(parents=True, exist_ok=True)
#
#     output_path = os.path.join(output_base_dir, file_name)
#     create_pdf(input_file, output_path, 'English')
#     print(f"PDF created: {os.path.join(output_base_dir, file_name)}")
