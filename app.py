import streamlit as st
import streamlit.components.v1 as components
import os

# 1. 페이지 기본 설정 (브라우저 탭 이름, 아이콘, 넓은 레이아웃)
st.set_page_config(
    page_title="영어 교사 AI 마스터 클래스",
    page_icon="🌸",
    layout="wide"
)

# 2. 상단 Streamlit 기본 메뉴 및 여백 제거 (HTML이 화면에 꽉 차 보이게 함)
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {
        padding-top: 0rem;
        padding-bottom: 0rem;
        padding-left: 0rem;
        padding-right: 0rem;
    }
    iframe {
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

def load_html():
    # 3. htmls 폴더 내 index.html 파일 경로 설정
    file_path = os.path.join("htmls", "index.html")
    
    # 4. 파일 존재 여부 확인 후 읽기 (한글 깨짐 방지를 위해 utf-8 인코딩)
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    else:
        st.error(f"파일을 찾을 수 없습니다: {file_path}")
        st.warning("app.py 파일과 같은 위치에 'htmls' 폴더를 만들고, 그 안에 'index.html' 파일이 있는지 확인해 주세요!")
        return None

# 5. HTML 불러오기 및 화면 렌더링
html_content = load_html()

if html_content:
    # PC/노트북 환경에서 스크롤이 자연스럽게 작동하도록 높이를 넉넉히 설정
    # components.html은 iframe으로 띄워지므로 scrolling=True로 설정합니다.
    components.html(html_content, height=1200, scrolling=True)
