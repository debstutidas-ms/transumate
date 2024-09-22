import time
from pathlib import Path
import os
import pdf2ImageConverter
from ocr import image_ocr
from text_extractor import extract_text_from_pdf
# from translator.ollama_translator import translate
from translator.transformer_tranlator import translate

from summarizer.summarizer import summarize
# from pdfGenerator import create_pdf
from PdfGenerator.reportlab.reportlab_translator import create_pdf

from concurrent.futures import ThreadPoolExecutor, as_completed


# BASE_PATH = r"C:\\Users\\debstutidas\\OneDrive - Microsoft\\Documents\\Hackathon\\Transumate\\transumate\\src"
BASE_PATH = "/Users/debstutidas/Documents/MLProjects/transumate/src"
DOCUMENT_PATH = 'Document'


def process_file(file_name, source_language):
    pdf_path = os.path.join(BASE_PATH, DOCUMENT_PATH, file_name)
    text = extract_text_from_pdf(pdf_path)
    txt_file_name = file_name[:-4]+'.txt'
    source_output_path = os.path.join(BASE_PATH, 'Source', source_language, txt_file_name)
    Path(os.path.join(BASE_PATH, 'Source', source_language)).mkdir(parents=True, exist_ok=True)
    with open(source_output_path, 'w+') as f:
        f.write(text)


def translate_file(file_name, source_language, dest_language):
    print(f'translating from {source_language} to {dest_language}')
    file_name = file_name[:-4]
    source_text_path = os.path.join(BASE_PATH, 'Source', source_language, file_name+'.txt')
    print(source_text_path, source_language, dest_language)
    return translate(source_text_path, source_language, dest_language)


def summarize_file(file_name, summary_language):
    print(f'summarizing  {file_name} in {summary_language}')
    source_file_name = f'{file_name[:-4]}_{summary_language}.txt'
    source_path = os.path.join(BASE_PATH, 'TranslationOutputs', source_file_name)
    summary_output_path = os.path.join(BASE_PATH, 'SummaryOutputs', source_file_name)

    with open(source_path, "r") as f:
        source_text = f.read()
        print('source text ', source_text)
        summary = summarize(source_text, summary_language)
        # print(translated)

        with open(summary_output_path, "w") as f:
            f.write(summary)

        return generate_pdf(summary_output_path, summary_language, 'summary')


def generate_pdf(txt_file, language, mode):

    if mode == 'summary':
        file_name = txt_file.split('/')[-1][:-4] + '_Summary.pdf'
        output_pdf_path = os.path.join(BASE_PATH, 'SummaryPdfs', file_name)

    elif mode == 'translation':
        file_name = txt_file.split('/')[-1][:-4] + '.pdf'
        output_pdf_path = os.path.join(BASE_PATH, 'TranslatedPdfs', file_name)
    else:
        output_pdf_path = 'Error'
        print('mode ', mode)

    create_pdf(txt_file, output_pdf_path, language)
    return output_pdf_path, file_name


