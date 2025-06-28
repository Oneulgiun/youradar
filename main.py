import streamlit as st

# 세션 상태 초기화
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

def login():
    st.title("🔐 YouRadar Access")
    password = st.text_input("비밀번호를 입력하세요", type="password")
    login_btn = st.button("로그인")

    if login_btn:
        if password == "you2025!":
            st.session_state.authenticated = True
            st.experimental_rerun()  # 🔁 로그인 성공 시 새로고침
        else:
            st.error("비밀번호가 틀렸습니다.")

# 로그인 안 했으면 로그인 화면만 보이게
if not st.session_state.authenticated:
    login()
    st.stop()

# 로그인 성공 후 화면
st.title("📍 YouRadar v0.1")
st.write("키워드 기반 유튜브 영상 검색 + 썸네일 추출 + CSV 저장 기능이 포함된 분석 툴입니다.")
st.info("이곳에 YouTube API 연동 및 필터 기능 추가 예정.")
