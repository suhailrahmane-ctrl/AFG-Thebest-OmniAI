import streamlit as st
import requests

st.set_page_config(page_title="AFG Thebest OmniAI – DeepSeek Version", layout="centered")
st.title("AFG Thebest OmniAI – DeepSeek Version")
st.write("چت پیشرفته با هوش مصنوعی – قدرت گرفته از **DeepSeek**")

# گرفتن کلید از Secrets
api_key = st.secrets["DEEPSEEK_API_KEY"]

# ورودی کاربر
user_input = st.text_input("پیامت را بنویس سهیل جان:")

if st.button("📩 ارسال") and user_input:
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": user_input}]
    }
    
    try:
        response = requests.post(
            "https://api.deepseek.com/chat/completions",
            headers=headers,
            json=data,
            timeout=20
        )
        if response.status_code == 200:
            result = response.json()
            answer = result['choices'][0]['message']['content']
            st.markdown(f"🤖 **هوش مصنوعی:** {answer}")
        else:
            st.error(f"خطا: {response.status_code} - {response.text}")
    except Exception as e:
        st.error(f"مشکل در ارتباط با API: {e}")
