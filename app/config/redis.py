import redis
import json
from app.config.config import REDIS_IP, REDIS_PORT, REDIS_PASSWORD

redis_client = redis.Redis(
    host = REDIS_IP,
    port = REDIS_PORT,
    decode_responses = True
)

def get_chat_history(userId):
    history = redis_client.get(userId)
    return json.loads(history) if history else []
    # if history:
    #     return json.loads(history)
    # else: 
    #     return []

def save_chat_history(userId, message):
    redis_client.set(
        userId, 
        json.dumps(message), 
        ex=3600  # 1 hour expiry (optional)
    )