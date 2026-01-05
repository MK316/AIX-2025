import streamlit as st

st.set_page_config(page_title="보고서 목차", layout="wide")

st.title("목  차")

# ✅ 1) GitHub 레포/브랜치 기본 주소 (본인 것으로 수정)
BASE = "https://github.com/MK316/AIX-2025/blob/main/pages/"


# ✅ 2) 섹션별 md 파일 경로 (레포 안의 상대 경로로 수정)
FILES = {
    "Ⅰ. 서론": "section01.md",
    "Ⅱ. 환경 분석": "section02.md",
    "Ⅲ. 요구분석": "section03.md",
    "Ⅳ. 국내외 대학 AI 교육과정 사례 분석": "section04.md",
    "Ⅴ. 교육목표 및 전공역량 설정": "section05.md",
    "Ⅵ. 전공교육과정 역량체계 구성": "section06.md",
    "Ⅶ. 단계별 교육과정 구조 및 교과목 실라버스": "section07.md",
    "Ⅷ. 교육과정 로드맵": "section08.md",
    "Ⅸ. 결론": "section09.md",
    "참고문헌": "references.md",
}

# ---------------------------
# Render: clickable TOC
# ---------------------------
st.markdown("### 📑 목차 (클릭하면 GitHub의 md 파일로 이동)")

for title, path in FILES.items():
    url = BASE + path
    st.markdown(f"- <a href='{url}' target='_blank'>{title}</a>", unsafe_allow_html=True)

st.markdown("---")
st.caption("※ 범례: 굵은체 = 수정사항, 붉은색 = 새로 추가한 내용")
