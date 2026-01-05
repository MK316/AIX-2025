import streamlit as st

st.set_page_config(page_title="보고서 목차", layout="wide")

st.title("목  차")

# ---------------------------
# TOC items only (no links)
# ---------------------------
TOC = [
    "Ⅰ. 서론",
    "Ⅱ. 환경 분석",
    "Ⅲ. 요구분석",
    "Ⅳ. 국내외 대학 AI 교육과정 사례 분석",
    "Ⅴ. 교육목표 및 전공역량 설정",
    "Ⅵ. 전공교육과정 역량체계 구성",
    "Ⅶ. 단계별 교육과정 구조 및 교과목 실라버스",
    "Ⅷ. 교육과정 로드맵",
    "Ⅸ. 결론",
    "참고문헌",
]


for item in TOC:
    st.markdown(f"{item}")

st.markdown("---")
st.caption("※ 범례: 굵은체 = 수정사항, 붉은색 = 새로 추가한 내용")
