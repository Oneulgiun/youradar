import streamlit as st

if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

def login():
    st.title("🔐 YouRadar Access")
    with st.form("login_form", clear_on_submit=True):
        password = st.text_input("비밀번호를 입력하세요", type="password")
        submitted = st.form_submit_button("로그인")
        if submitted:
            if password == "you2025!":
                st.session_state.authenticated = True
                st.experimental_rerun()
            else:
                st.error("비밀번호가 틀렸습니다.")

if not st.session_state.authenticated:
    login()
    st.stop()

st.title("📍 YouRadar v0.1")
st.write("키워드 기반 유튜브 영상 검색 + 썸네일 추출 + CSV 저장 기능이 포함된 분석 툴입니다.")
st.info("이곳에 YouTube API 연동 및 필터 기능 추가 예정.")
