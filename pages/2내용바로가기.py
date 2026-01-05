import streamlit as st
import requests

st.set_page_config(page_title="AI-X 보고서", layout="wide")

# -----------------------------
# 1) GitHub RAW base (중요)
# -----------------------------
RAW_BASE = "https://raw.githubusercontent.com/MK316/AIX-2025/main/pages/"

# -----------------------------
# 2) Sidebar menu -> file map
# -----------------------------
SECTIONS = {
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

st.sidebar.title("📑 목차")
selected = st.sidebar.radio("섹션 선택", list(SECTIONS.keys()), index=0)

# -----------------------------
# 3) Fetch & render markdown
# -----------------------------
@st.cache_data(show_spinner=False)
def fetch_md(url: str) -> str:
    r = requests.get(url, timeout=15)
    r.raise_for_status()
    return r.text

md_url = RAW_BASE + SECTIONS[selected]

try:
    md_text = fetch_md(md_url)
    st.markdown(md_text, unsafe_allow_html=True)
except Exception as e:
    st.error("Markdown 파일을 불러오지 못했습니다.")
    st.code(str(e))
    st.markdown(f"요청 URL: {md_url}")
