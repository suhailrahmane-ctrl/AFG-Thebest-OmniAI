import streamlit as st
import openai
import os

# گرفتن کلید API از محیط Streamlit
openai.api_key = os.environ.get("OPENAI_API_KEY")

def chat_ui():
    user_input = st.text_input("پیام خودت را وارد کن:")
    if st.button("ارسال"):
        if user_input.strip() == "":
            st.warning("پیام خالی است!")
            return
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role":"user","content":user_input}]
            )
            st.write(response.choices[0].message.content)
        except Exception as e:
            st.error(f"مشکل پیش آمد: {e}")
