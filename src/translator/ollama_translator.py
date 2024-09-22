from langchain import PromptTemplate
from langchain_community.llms import Ollama


class OllamaModelForTranslation:
    def __init__(self):
        # Ollama LLM
        self.llm = Ollama(model='llama3')
        self.prompt = PromptTemplate.from_template("Translate the given text from source language {source_lang} to "
                                                   "dest {dest_lang}. Input text: {text}")

    def invoke(self, source_language, dest_language, text):
        # create the prompt, here we use multiple inputs

        # format the prompt to add variable values
        prompt_formatted_str: str = self.prompt.format(
            source_lang=source_language,
            dest_lang=dest_language,
            text=text)

        # make a prediction
        return self.llm.predict(prompt_formatted_str)


ollama = OllamaModelForTranslation()


def translate(text:str, src_lang: str, dest_lang: str, mode='ollama') -> str:
    return ollama.invoke(src_lang, dest_lang, text)
