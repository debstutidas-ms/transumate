from googletrans import Translator

translator = Translator()


def translate(text):
    return translator.translate(text,  src='bn').text


# from deep_translator import GoogleTranslator
# GoogleTranslator(source='auto', target='de').translate("keep it up, you are awesome")
# 'weiter so, du bist toll'