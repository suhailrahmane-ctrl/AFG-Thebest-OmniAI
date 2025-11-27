import streamlit as st
import replicate
import os

# اتصال به Replicate با کلید API
replicate_client = replicate.Client(api_token=os.environ.get("REPLICATE_API_KEY"))

def image_ui():
    prompt = st.text_input("چه تصویری می‌خوای بسازی؟")
    if st.button("تولید تصویر"):
        if prompt.strip() == "":
            st.warning("لطفاً یک متن وارد کن!")
            return
        with st.spinner("در حال ساخت تصویر..."):
            try:
                output = replicate_client.run(
                    "stability-ai/stable-diffusion:latest",
                    input={"prompt": prompt}
                )
                st.image(output[0], caption="تصویر ساخته شده")
            except Exception as e:
                st.error(f"مشکل پیش آمد: {e}")
