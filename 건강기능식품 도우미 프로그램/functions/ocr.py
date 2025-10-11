import streamlit as st
import pandas as pd
import requests
import uuid
import time
import json
import os
from dotenv import load_dotenv

@st.cache_data
def load_ingredient_db():
    # 현재 파일의 디렉토리를 기준으로 데이터 파일 경로 설정
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(current_dir, "..", "data", "ingredient_db.csv")
    df = pd.read_csv(data_path)
    df = df.dropna(subset=['성분'])
    df['성분'] = df['성분'].astype(str).str.strip()
    return df

def extract_text_from_image(image_file):
    load_dotenv()
    
    api_url = 'https://4d47g9kt53.apigw.ntruss.com/custom/v1/42405/9dc17f748f42c61c17a4201de6a6a9054f5e87ac699453cc88d1fa091e1d0c6d/general'
    secret_key = os.getenv("OCR_SECRET_KEY")
    
    if not secret_key:
        raise ValueError("OCR_SECRET_KEY가 설정되지 않았습니다. .env 파일을 확인해주세요.")

    request_json = {
        'images': [{'format': 'jpg', 'name': 'demo'}],
        'requestId': str(uuid.uuid4()),
        'version': 'V2',
        'timestamp': int(round(time.time() * 1000))
    }

    payload = {'message': json.dumps(request_json).encode('UTF-8')}
    files = [('file', image_file)]
    headers = {'X-OCR-SECRET': secret_key}

    response = requests.post(api_url, headers=headers, data=payload, files=files)
    result_json = response.json()

    return [field['inferText'] for field in result_json['images'][0]['fields']]

def run():
    st.header("🧾 OCR 기반 성분 추출기")

    uploaded_file = st.file_uploader("이미지 파일을 업로드하세요", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption="업로드된 이미지", use_container_width=True)

        if st.button("성분 추출 시작"):
            with st.spinner("OCR 인식 및 성분 분석 중..."):
                try:
                    extracted_texts = extract_text_from_image(uploaded_file)
                    ingredient_df = load_ingredient_db()
                    ingredient_list = ingredient_df['성분'].tolist()

                    matched_info = []
                    for text in extracted_texts:
                        for ingredient in ingredient_list:
                            if ingredient in text:
                                func_text = ingredient_df[ingredient_df['성분'] == ingredient]['기능성 내용'].values
                                func_text = func_text[0] if len(func_text) > 0 else "정보 없음"
                                matched_info.append((ingredient, func_text))
                                break  # 하나의 텍스트에서 여러 성분이 중복 매칭되는 것 방지

                    st.subheader("✅ 매칭된 성분 및 기능성 내용")
                    if matched_info:
                        for name, func in matched_info:
                            st.markdown(f"**🧬 {name}**")
                            st.markdown(f"→ {func}")
                    else:
                        st.warning("성분 데이터베이스와 일치하는 항목이 없습니다.")

                except Exception as e:
                    st.error(f"OCR 처리 중 오류 발생: {e}")

