import streamlit as st
import pandas as pd
from utils.prompt_utils import generate_prompt
from utils.openai_utils import get_llm_response

@st.cache_data
def load_data():
    import os
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(current_dir, "..", "data", "기능23_data.csv")
    return pd.read_csv(data_path)

def run():
    st.subheader("🏷️ 마케팅 문구 추천 시스템")
    df = load_data()
    

    options = df['성분'].tolist()
    selected = st.selectbox("성분을 선택하세요", options)
    row = df[df['성분'] == selected].iloc[0]
    기능설명 = row['기능성 내용']
    표현가능사례 = row['표현가능사례']
    어려운사례 = row['표현하기 어려운 사례']

    if st.button("문구 생성"):
        prompt = generate_prompt(selected, 기능설명, 표현가능사례, 어려운사례)
        
        with st.spinner("문구 생성 중..."):
            result = get_llm_response(prompt)
            st.success("문구 예시:")
            st.markdown(result)
