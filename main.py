import streamlit as st

# 세션 상태 초기화
if "password_correct" not in st.session_state:
    st.session_state.password_correct = False

def password_gate():
    st.title("🔐 YouRadar Access")
    password = st.text_input("비밀번호를 입력하세요", type="password")
    
    if password == "":
        st.stop()

    if password == "you2025!":
        st.session_state.password_correct = True
    else:
        st.error("비밀번호가 틀렸습니다.")
        st.stop()

# 인증 여부 확인
if not st.session_state.password_correct:
    password_gate()

# 통과한 사람만 보이는 화면
st.title("🎯 YouRadar v0.1")
st.write("키워드 기반 유튜브 영상 검색 + 썸네일 추출 + CSV 저장 기능이 포함된 분석 툴입니다.")
st.info("이곳에 YouTube API 연동 및 필터 기능 추가 예정.")
