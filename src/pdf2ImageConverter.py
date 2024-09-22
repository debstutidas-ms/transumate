import os
from pathlib import Path
from pdf2image import convert_from_path

DOCUMENT_IMAGES_PATH = 'SrcImages'


def convert_pdf_2_images(base_path, document_path, filename):
    pdf_path = os.path.join(base_path, document_path, filename)

    # Store Pdf with convert_from_path function
    images = convert_from_path(pdf_path)
    document_images_path = f'{DOCUMENT_IMAGES_PATH}/{filename}'
    print(str(len(images))+' images')
    Path(document_images_path).mkdir(parents=True, exist_ok=True)
    for i in range(len(images)):
        # Save pages as images in the pdf
        images[i].save(f'{document_images_path}/page{i}.png', 'PNG')
        print('saved ', f'{document_images_path}/page{i}.png')
    return len(images), document_images_path


def convert_pdf_bytes_2_images(pdf_bytes):

    # Store Pdf with convert_from_path function
    images = convert_from_path(pdf_bytes)
    document_images_path = f'{DOCUMENT_IMAGES_PATH}/test'

    Path(document_images_path).mkdir(parents=True, exist_ok=True)
    for i in range(len(images)):
        # Save pages as images in the pdf
        images[i].save(f'{document_images_path}/page{i}.png', 'PNG')
    return len(images), document_images_path
