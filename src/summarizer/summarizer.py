from langchain import PromptTemplate
from langchain_community.llms import Ollama


class OllamaModelForSummarization:
    def __init__(self):
        # Ollama LLM
        self.llm = Ollama(model='llama3')
        self.prompt = PromptTemplate.from_template("Summarize the given text in 100 to max 200 words in language:"
                                                   " {language}. text: {text}")

    def invoke(self, text, language):

        # format the prompt to add variable values
        prompt_formatted_str: str = self.prompt.format(language=language, text=text)

        # make a prediction
        return self.llm.predict(prompt_formatted_str)


ollama = OllamaModelForSummarization()


def summarize(text: str, language: str) -> str:
    return ollama.invoke(text, language)



