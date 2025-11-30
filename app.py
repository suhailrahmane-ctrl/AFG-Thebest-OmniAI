import streamlit as st
import requests

st.set_page_config(page_title="AFG Thebest OmniAI – OpenRouter Version", page_icon="🤖")

st.title("AFG Thebest OmniAI – OpenRouter Version")
st.write("چت پیشرفته با هوش مصنوعی – قدرت گرفته از OpenRouter")

OPENROUTER_API_KEY = st.secrets["OPENROUTER_API_KEY"]

user_message = st.text_input("پیامت را بنویس سهیل جان:")

if st.button("📩 ارسال"):
    if not user_message:
        st.error("لطفاً پیام بنویس!")
    else:
        url = "https://openrouter.ai/api/v1/chat/completions"

        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "HTTP-Referer": "https://afg-thebest-omniai.streamlit.app",
            "X-Title": "AFG Thebest OmniAI"
        }

        data = {
            "model": "openai/gpt-4o-mini",
            "messages": [
                {"role": "user", "content": user_message}
            ]
        }

        try:
            response = requests.post(url, headers=headers, json=data)

            if response.status_code == 200:
                answer = response.json()["choices"][0]["message"]["content"]
                st.success(answer)
            else:
                st.error(f"خطا: {response.status_code}")
                st.error(response.text)

        except Exception as e:
            st.error(f"خطای غیرمنتظره: {str(e)}")
