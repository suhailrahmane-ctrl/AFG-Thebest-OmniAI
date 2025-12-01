import os

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

MODEL_NAME = "deepseek/deepseek-chat"

HEADERS = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "HTTP-Referer": "https://afg-thebest-omniai.streamlit.app/",
    "X-Title": "AFG Thebest OmniAI"
}
