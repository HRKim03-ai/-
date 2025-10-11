import streamlit as st
from functions.ocr import run as run_ocr
from functions.generator import run as run_gen
from functions.checker import run as run_chk

st.set_page_config(page_title="건강기능식품 도우미", page_icon="💊")
st.title("💊 건강기능식품 도우미 프로그램")

option = st.radio("기능을 선택하세요", ["🧾 OCR 기반 정확한 기능 안내", "🏷️ 마케팅 문구 생성", "🚨 허위·과장 문구 판별"])


if option == "🧾 OCR 기반 정확한 기능 안내":
    run_ocr()
elif option == "🏷️ 마케팅 문구 생성":
    run_gen()
elif option == "🚨 허위·과장 문구 판별":
    run_chk()
