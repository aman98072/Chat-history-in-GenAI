from app.config.redis import get_chat_history, save_chat_history

system_prompt = {
    "role": "system",
    "content": (
        "You are a conversational AI with memory. "
        "Use previous user messages to answer follow-up questions. "
        "Do NOT hallucinate memory. "
        "If information is not present in history, say you don't know."
    )
}

def prompt(query, user_id):
    # Get history from Redis
    history = get_chat_history(user_id) or []

    # Append new user message
    history.append({
        "role": "user",
        "content": query
    })

    # Save updated history back to Redis
    save_chat_history(user_id, history)

    # Build final messages for LLM
    messages = [system_prompt] + history

    return messages
