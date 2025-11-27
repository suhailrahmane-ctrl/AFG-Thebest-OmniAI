import streamlit as st
from components.chat_component import chat_ui
from components.image_component import image_ui

# تنظیمات صفحه
st.set_page_config(page_title="AFG Omniverse AI", layout="wide")
st.title("AFG Omniverse AI")

# بخش چت با هوش مصنوعی
st.header("چت با هوش مصنوعی")
chat_ui()

# بخش تولید تصویر با هوش مصنوعی
st.header("تولید تصویر با هوش مصنوعی")
image_ui()
