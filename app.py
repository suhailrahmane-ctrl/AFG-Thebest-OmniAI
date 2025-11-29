import streamlit as st
import requests
from model_config import MODEL_NAME

# عنوان و توضیح اپلیکیشن
st.set_page_config(page_title="AFG Thebest OmniAI", page_icon="🤖")
st.title("AFG Thebest OmniAI – DeepSeek Version")
st.write("چت پیشرفته با هوش مصنوعی – قدرت گرفته از **DeepSeek**")

# گرفتن کلید API از Secrets
try:
    api_key = st.secrets["DEEPSEEK_API_KEY"]
except KeyError:
    st.error("کلید DEEPSEEK_API_KEY پیدا نشد! لطفاً در Secrets اضافه کنید.")
    st.stop()

# ورودی کاربر
user_input = st.text_input("پیامت را بنویس سهیل جان:")

# ارسال پیام و دریافت پاسخ
if st.button("📩 ارسال"):
    if not user_input:
        st.warning("لطفاً پیام خود را وارد کنید!")
    else:
        try:
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
                },
                timeout=20  # زمان انتظار پاسخ
            )

            data = response.json()

            if "choices" in data and len(data["choices"]) > 0:
                bot_reply = data["choices"][0]["message"]["content"]
                st.markdown(f"🤖 **هوش مصنوعی:** {bot_reply}")
            else:
                st.error("متاسفم، پاسخ دریافت نشد. لطفاً دوباره تلاش کنید.")

        except requests.exceptions.RequestException as e:
            st.error(f"خطا در ارتباط با DeepSeek API: {e}")
        except Exception as e:
            st.error(f"خطای ناشناخته: {e}")
