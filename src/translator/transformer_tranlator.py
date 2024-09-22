import os
from transformers import pipeline


BASE_PATH = "/Users/debstutidas/Documents/MLProjects/transumate/src"

lang_codes = {
    'Spanish': 'es', 'German': 'de', 'English': 'en', 'Hindi': 'hi', 'Kannada': 'kn'}


def translate(input_file, source_language, dest_language):
    file_name = input_file.split('/')[-1]
    print(source_language, dest_language)
    model_name = f'Helsinki-NLP/opus-mt-{lang_codes[source_language]}-{lang_codes[dest_language]}'
    translator = pipeline("translation", model=model_name)  # for example English to French
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()

    # Translate the text in chunks (if it's large)
    translated_text = []
    max_length = 512  # Maximum length for translation models

    for i in range(0, len(text), max_length):
        chunk = text[i:i + max_length]
        translation = translator(chunk)
        translated_text.extend(translation)

    # Save the translated text to a new file
    output_file_name = '_'.join(file_name.split('_')[:-1])+'_'+dest_language+'.txt'
    print('op translated txt file ',output_file_name )
    output_file_path = os.path.join(BASE_PATH, 'TranslationOutputs', output_file_name)
    with open(output_file_path, 'w', encoding='utf-8') as file:
        for translation in translated_text:
            file.write(translation['translation_text'] + "\n")
    return output_file_path


# translate( 'Spanish', 'English', '/Users/debstutidas/Documents/MLProjects/transumate/src/Samples/TXT/spanish.txt')

