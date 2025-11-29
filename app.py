import streamlit as st
from groq import Groq
import os

st.set_page_config(page_title="AFG Thebest OmniAI", page_icon="🤖")

st.title("🤖 AFG Thebest OmniAI")
st.write("چت پیشرفته با هوش مصنوعی – قدرت گرفته از **Groq LLM**")

# گرفتن کلید از Secrets
GROQ_API_KEY = st.secrets.get("GROQ_API_KEY")

if not GROQ_API_KEY:
    st.error("❌ کلید API تنظیم نشده! لطفاً داخل تنظیمات Streamlit → Secrets کلید را اضافه کنید.")
    st.stop()

client = Groq(api_key=GROQ_API_KEY)

# ورودی کاربر
user_input = st.text_input("پیامت را بنویس سهیل جان:")

if st.button("📩 ارسال"):
    if not user_input.strip():
        st.warning("لطفاً پیام بنویس!")
    else:
        try:
            chat_completion = client.chat.completions.create(
                model="gemma-7b-it",  # مدل رایگان و قابل استفاده
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_input}
                ],
                max_tokens=300,
            )

            reply = chat_completion.choices[0].message["content"]
            st.write("🤖 **هوش مصنوعی:**", reply)

        except Exception as e:
            st.error("❌ متاسفم، پاسخ در دسترس نیست.")
