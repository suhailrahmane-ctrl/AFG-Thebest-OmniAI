import streamlit as st
import requests
import json

st.set_page_config(page_title="AFG Thebest OmniAI", page_icon="🤖")

DEEPSEEK_API_KEY = st.secrets["DEEPSEEK_API_KEY"]

st.title("🤖 AFG Thebest OmniAI")
st.write("چت پیشرفته با هوش مصنوعی – قدرت گرفته از DeepSeek")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_msg = st.text_input("پیامت را بنویس سهیل جان:")

if st.button("📩 ارسال"):

    if user_msg.strip() == "":
        st.error("لطفاً یک پیام بنویس!")
    else:
        st.session_state.messages.append({"role": "user", "content": user_msg})

        try:
            url = "https://api.deepseek.com/chat/completions"

            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {DEEPSEEK_API_KEY}"
            }

            payload = {
                "model": "deepseek-chat",
                "messages": st.session_state.messages,
                "temperature": 0.7,
                "max_tokens": 300
            }

            response = requests.post(url, headers=headers, data=json.dumps(payload))
            result = response.json()

            # جواب هوش مصنوعی
            bot_reply = result["choices"][0]["message"]["content"]

            st.session_state.messages.append({"role": "assistant", "content": bot_reply})

        except Exception as e:
            st.error("پاسخ دریافت نشد! احتمالاً کلید یا مدل اشتباه است.")
            st.write(e)

# نمایش چت
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"🧑 **تو:** {msg['content']}")
    else:
        st.markdown(f"🤖 **هوش مصنوعی:** {msg['content']}")
