import requests

API_KEY = "اینجا کلید واقعی DeepSeek را بگذار"

url = "https://api.deepseek.com/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

data = {
    "model": "deepseek-chat",
    "messages": [
        {"role": "user", "content": "سلام، تست API هستی؟"}
    ]
}

response = requests.post(url, json=data, headers=headers)

print("Status code:", response.status_code)
print("Response:", response.text)
