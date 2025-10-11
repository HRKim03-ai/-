import streamlit as st
import pandas as pd
from utils.openai_utils import get_llm_response as generate_phrases
from utils.prompt_utils import warning_prompt

@st.cache_data
def load_data():
    import os
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(current_dir, "..", "data", "기능23_data.csv")
    return pd.read_csv(data_path)

def run():
    st.header("🚨 광고 문구 경고")

    df = load_data()

    st.subheader("광고 문구 검수 시스템🤖")
    st.markdown('과장.허위.잘못된 정보를 담은 광고문구가 의심된다면 주요 성분과 문구를 입력해주세요!')
    options = df['성분'].tolist()
    selected = st.multiselect("성분을 선택하세요:", options)

    if selected:
        selected_rows = df[df['성분'].isin(selected)]

        기능설명 = "\n".join(selected_rows['기능성 내용'].tolist())
        어려운사례_list = selected_rows['표현하기 어려운 사례'].tolist()
        어려운사례_unique = list(set(어려운사례_list))
        어려운사례 = "\n".join(어려운사례_unique)
    else:
        기능설명 = ""
        어려운사례 = ""

    # 사용자 입력 문구
    user_input = st.text_area("검사할 광고 문구를 입력하세요:")

    if st.button("검사 시작"):
        if not user_input.strip():
            st.warning("문구를 입력해 주세요.")
        else:
            with st.spinner("검사 중..."):
                prompt_check = warning_prompt(user_input, 기능설명, 어려운사례)
                result_check = generate_phrases(prompt_check)

                if "안전함" in result_check or "문제 없습니다" in result_check:
                    st.success("✅ 문구에 문제가 없습니다!")
                else:
                    st.error(f"🚨 경고: {result_check}")

