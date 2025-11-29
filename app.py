import streamlit as st
from groq import Groq

# --- خواندن API Key از Streamlit Secrets ---
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

# --- ایجاد کلاینت Groq ---
client = Groq(api_key=GROQ_API_KEY)

# --- رابط کاربری Streamlit ---
st.set_page_config(page_title="AFG Thebest OmniAI Chat", page_icon="🤖", layout="centered")

st.title("🤖 AFG Thebest OmniAI")
st.write("چت پیشرفته با هوش مصنوعی – قدرت گرفته از **Groq LLM**")

# --- دریافت پیام کاربر ---
user_input = st.text_input("پیامت را بنویس سهیل جان:", "")

# --- ذخیره تاریخچه پیام‌ها ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- نمایش تاریخچه پیام‌ها ---
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"🧑 **تو:** {msg['content']}")
    else:
        st.markdown(f"🤖 **هوش مصنوعی:** {msg['content']}")

# --- ارسال پیام کاربر و دریافت پاسخ ---
if st.button("📩 ارسال"):
    if user_input.strip() != "":
        # ذخیره پیام کاربر
        st.session_state.messages.append({"role": "user", "content": user_input})

        # تماس با Groq AI
        chat_completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You are AFG Thebest OmniAI, a friendly AI assistant."},
                {"role": "user", "content": user_input},
            ],
            max_tokens=300,
        )

        # دریافت پاسخ بدون خطا با توجه به نسخه جدید Groq
        try:
            bot_reply = chat_completion.choices[0].message["content"]
        except (AttributeError, TypeError):
            bot_reply = getattr(chat_completion, "output_text", "متاسفم، پاسخ در دسترس نیست.")

        # ذخیره پاسخ
        st.session_state.messages.append({"role": "assistant", "content": bot_reply})

        # بروزرسانی رابط
        st.rerun()
