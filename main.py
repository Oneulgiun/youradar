import streamlit as st

def password_gate():
    st.title("🔐 YouRadar Access")
    password = st.text_input("비밀번호를 입력하세요", type="password")

    # 공백 제거한 비밀번호 검사
    if password.strip() == "you2025!":
        return True
    elif password:  # 틀렸을 때
        st.error("❌ 비밀번호가 틀렸습니다.")
        st.stop()
    else:
        st.stop()  # 아무것도 안 쳤을 때

# 비밀번호 통과한 사람만 진입
if password_gate():
    st.title("🎯 YouRadar v0.1")
    st.write("키워드 기반 유튜브 영상 검색 + 썸네일 추출 + CSV 저장 기능이 포함된 분석 툴입니다.")
    st.info("이곳에 YouTube API 연동 및 필터 기능 추가 예정.")
