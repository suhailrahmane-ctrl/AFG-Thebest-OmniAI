import os

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")  # یا مستقیم کلیدت را اینجا بگذار

MODEL_NAME = "openrouter/gpt-4"  # یا مدل OpenRouter که داری

HEADERS = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}"
}
