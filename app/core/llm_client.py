from app.config.constant import TEMPERATURE, MAX_TOKENS, MODEL_NAME
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq()

def llmResponse(messages, model = MODEL_NAME, temperature = TEMPERATURE, max_tokens = MAX_TOKENS):
    result = client.chat.completions.create(
        model = model,
        temperature = temperature,
        max_tokens = max_tokens,
        messages = messages
    )

    return result.choices[0].message.content 