import requests
import os

def post_webhook(content: str):
    requests.post(os.getenv("WEBHOOK_URL"), json={"content": content})