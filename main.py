import streamlit as st

# 세션 상태 초기화
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'password_input' not in st.session_state:
    st.session_state.password_input = ""

def login():
    st.title("🔐 YouRadar Access")
    # 비밀번호 입력값을 세션에 저장
    st.session_state.password_input = st.text_input("비밀번호를 입력하세요", type="password")

    if st.button("로그인"):
        if st.session_state.password_input == "you2025!":
            st.session_state.authenticated = True
            st.experimental_rerun()
        else:
            st.error("비밀번호가 틀렸습니다.")

# 로그인하지 않았다면 로그인 창만 보이게
if not st.session_state.authenticated:
    login()
    st.stop()

# 로그인 성공 시 보여줄 화면
st.title("📍 YouRadar v0.1")
st.write("키워드 기반 유튜브 영상 검색 + 썸네일 추출 + CSV 저장 기능이 포함된 분석 툴입니다.")
st.info("이곳에 YouTube API 연동 및 필터 기능 추가 예정.")
