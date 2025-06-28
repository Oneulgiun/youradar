import streamlit as st

def password_gate():
    st.title("🔐 YouRadar Access")
    password = st.text_input("비밀번호를 입력하세요", type="password")
    if password == "you2025!":
        return True
    st.error("비밀번호가 틀렸습니다.")
    return False

if password_gate():
    st.title("🎯 YouRadar v0.1")
    st.write("키워드 기반 유튜브 영상 검색 + 썸네일 추출 + CSV 저장 기능이 포함된 분석 툴입니다.")
    # 이후 기능은 여기에 붙여넣기 (간단 버전)
    st.info("이곳에 YouTube API 연동 및 필터 기능 추가 예정.")
