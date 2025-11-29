import streamlit as st
import requests
import os
from model_config import MODEL_NAME

# عنوان
st.title("AFG Thebest OmniAI – DeepSeek Version")
st.write("چت پیشرفته با هوش مصنوعی – قدرت گرفته از **DeepSeek**")

# گرفتن کلید
api_key = st.secrets["DEEPSEEK_API_KEY"]

# ورودی کاربر
user_input = st.text_input("پیامت را بنویس سهیل جان:")

if st.button("📩 ارسال"):
    if not user_input:
        st.warning("لطفاً پیام بنویس!")
    else:
        try:
            # درخواست به DeepSeek
            response = requests.post(
                "https://api.deepseek.com/chat/completions",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {api_key}"
                },
                json={
                    "model": MODEL_NAME,
                    "messages": [
                        {"role": "user", "content": user_input}
                    ]
                }
            )

            data = response.json()

            # نمایش جواب
            if "choices" in data:
                bot_reply = data["choices"][0]["message"]["content"]
                st.write("🤖 **هوش مصنوعی:**")
                st.write(bot_reply)
            else:
                st.error("متاسفم، پاسخ دریافت نشد.")

        except Exception as e:
            st.error("خطا رخ داد. جزئیات در لاگ‌ها ثبت شد.")
