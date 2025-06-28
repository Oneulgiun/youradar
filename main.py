import streamlit as st

# 앱 제목
st.title("🔐 YouRadar Access")

# 비밀번호 입력
password = st.text_input("비밀번호를 입력하세요", type="password")

# 로그인 버튼
if st.button("로그인"):
    if password == "1234":  # 여기서 비밀번호 조건
        st.session_state["authenticated"] = True
    else:
        st.error("비밀번호가 틀렸습니다.")

# 로그인 성공 시 메인 페이지
if st.session_state.get("authenticated"):
    st.markdown("## 🎯 YouRadar v0.1")
    st.write("키워드 기반 유튜브 영상 검색+썸네일 추출+CSV 저장 기능이 포함된 분석 툴입니다.")
    st.info("이곳에 YouTube API 연동 및 필터 기능 추가 예정.")
