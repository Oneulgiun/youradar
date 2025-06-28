import streamlit as st

# 세션 상태 초기화
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

def login():
    st.title("🔐 YouRadar Access")

    with st.form("login_form"):
        password = st.text_input("비밀번호를 입력하세요", type="password")
        submit = st.form_submit_button("로그인")

        if submit:
            if password == "you2025!":
                st.session_state.authenticated = True
                st.experimental_rerun()
            else:
                st.error("비밀번호가 틀렸습니다.")

# 로그인하지 않은 경우
if not st.session_state.authenticated:
    login()
    st.stop()

# 로그인 성공 시 메인 화면
st.title("📍 YouRadar v0.1")
st.write("키워드 기반 유튜브 영상 검색 + 썸네일 추출 + CSV 저장 기능이 포함된 분석 툴입니다.")
st.info("이곳에 YouTube API 연동 및 필터 기능 추가 예정.")
