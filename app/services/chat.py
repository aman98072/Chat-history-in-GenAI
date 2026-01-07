from app.prompts.chat import prompt
from app.core.llm_client import llmResponse

def chat(text, id):
    modifiedPrompt = prompt(text, id)
    result = llmResponse(modifiedPrompt)
    return result
