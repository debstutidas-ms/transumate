from ollama_translator import OllamaModelForTranslation


ollama = OllamaModelForTranslation()


def translate(text:str, src_lang: str, dest_lang: str, mode='ollama') -> str:
    resp = ollama.invoke(src_lang, dest_lang, text)
    print(resp)

print(translate('hello', 'English', 'Bengali'))