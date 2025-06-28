import streamlit as st

# 페이지 설정
st.set_page_config(page_title="YouRadar Access", page_icon="🎯", layout="centered")

# 제목 영역
st.markdown("## 🔒 YouRadar Access")
st.markdown("비밀번호를 입력하세요")

# 비밀번호 입력
password = st.text_input(" ", type="password", label_visibility="collapsed")

# 로그인 버튼
if st.button("로그인"):
    if password == "sd1986":  # ✅ 여기에 네가 원하는 비번으로 바꿔도 돼
        st.success("✅ 로그인 성공!")

        st.markdown("---")
        st.markdown("## 🎯 YouRadar v0.1")
        st.markdown("키워드 기반 유튜브 영상 검색 + 썸네일 추출 + CSV 저장 기능이 포함된 분석 툴입니다.")
        st.info("이곳에 YouTube API 연동 및 필터 기능 추가 예정.")

        # 여기에 추후 기능 추가 (예: 검색창, 결과 출력 등)

    else:
        st.error("❌ 비밀번호가 틀렸습니다.")
