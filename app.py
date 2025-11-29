import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize Groq client
client = Groq(api_key=GROQ_API_KEY)

# Streamlit UI
st.set_page_config(page_title="AFG Thebest OmniAI Chat", page_icon="🤖", layout="centered")

st.title("🤖 AFG Thebest OmniAI")
st.write("چت پیشرفته با هوش مصنوعی – قدرت گرفته از **Groq LLM**")

# Chat input
user_input = st.text_input("پیامت را بنویس سهیل جان:", "")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show chat history
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"🧑 **تو:** {msg['content']}")
    else:
        st.markdown(f"🤖 **هوش مصنوعی:** {msg['content']}")

# When user sends message
if st.button("📩 ارسال"):
    if user_input.strip() != "":
        # Save user message
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Call Groq AI
        chat_completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",  
            messages=[
                {"role": "system", "content": "You are AFG Thebest OmniAI, a friendly AI assistant."},
                {"role": "user", "content": user_input},
            ],
            max_tokens=300,
        )

        bot_reply = chat_completion.choices[0].message["content"]

        # Save bot reply
        st.session_state.messages.append({"role": "assistant", "content": bot_reply})

        # Refresh UI
        st.rerun()
