import streamlit as st
from model_config import HEADERS, MODEL_NAME
import requests

# تنظیمات صفحه
st.set_page_config(page_title="AFG Thebest OmniAI", page_icon="🤖")
st.title("AFG Thebest OmniAI – Chat & Image")
st.markdown("چت پیشرفته و تولید عکس با هوش مصنوعی – قدرت گرفته از DeepSeek")

# ---------------------
# بخش چت
# ---------------------
st.header("💬 چت با هوش مصنوعی")
user_message = st.text_input("پیامت را بنویس سهیل جان:")

if st.button("ارسال پیام"):
    if user_message:
        with st.spinner("در حال پردازش پیام..."):
            try:
                url = "https://api.deepseek.ai/v1/chat/completions"
                payload = {
                    "model": MODEL_NAME,
                    "messages": [
                        {"role": "system", "content": "You are AFG Thebest OmniAI, a helpful multilingual assistant."},
                        {"role": "user", "content": user_message}
                    ],
                    "max_tokens": 300
                }
                response = requests.post(url, json=payload, headers=HEADERS)
                if response.status_code != 200:
                    st.error(f"خطا: {response.status_code} - {response.text}")
                else:
                    result = response.json()
                    answer = result["choices"][0]["message"]["content"]
                    st.markdown(f"🤖 هوش مصنوعی: {answer}")
            except Exception as e:
                st.error(f"خطا در دریافت پاسخ: {e}")

# ---------------------
# بخش تولید عکس
# ---------------------
st.header("🖼️ تولید عکس با هوش مصنوعی")
image_prompt = st.text_input("ایده عکس خود را وارد کن:")

if st.button("تولید عکس"):
    if image_prompt:
        with st.spinner("در حال تولید عکس..."):
            try:
                url_image = "https://api.deepseek.ai/v1/images/generations"
                payload_image = {
                    "prompt": image_prompt,
                    "size": "512x512",
                    "n": 1
                }
                response_image = requests.post(url_image, json=payload_image, headers=HEADERS)
                if response_image.status_code != 200:
                    st.error(f"خطا: {response_image.status_code} - {response_image.text}")
                else:
                    result_image = response_image.json()
                    img_url = result_image["data"][0]["url"]
                    st.image(img_url, caption=image_prompt)
            except Exception as e:
                st.error(f"خطا در تولید عکس: {e}")
