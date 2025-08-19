import streamlit as st
import random

# 색상 팔레트 (상의 → 나머지 아이템과 어울리는 색)
outfit_palette = {
    "화이트": {
        "하의": ["블랙", "데님 블루", "베이지", "카키"],
        "신발": ["화이트", "블랙", "그레이"],
        "가방": ["블랙", "브라운", "네이비"]
    },
    "블랙": {
        "하의": ["화이트", "그레이", "베이지"],
        "신발": ["블랙", "화이트", "레드"],
        "가방": ["화이트", "실버", "브라운"]
    },
    "베이지": {
        "하의": ["화이트", "네이비", "블랙"],
        "신발": ["브라운", "화이트", "블랙"],
        "가방": ["블랙", "브라운", "카키"]
    },
    "네이비": {
        "하의": ["화이트", "베이지", "그레이"],
        "신발": ["화이트", "블랙", "브라운"],
        "가방": ["옐로우", "화이트", "브라운"]
    },
    "그레이": {
        "하의": ["블랙", "화이트", "네이비"],
        "신발": ["화이트", "블랙", "민트"],
        "가방": ["블랙", "핑크", "네이비"]
    }
}

# 색상 코드
color_codes = {
    "화이트": "#FFFFFF",
    "블랙": "#000000",
    "그레이": "#808080",
    "베이지": "#F5F5DC",
    "네이비": "#000080",
    "레드": "#FF0000",
    "옐로우": "#FFD700",
    "핑크": "#FFC0CB",
    "브라운": "#8B4513",
    "카키": "#808000",
    "데님 블루": "#1E3A5F",
    "실버": "#C0C0C0",
    "민트": "#98FF98"
}

# 아이템 이미지 (URL 또는 로컬 파일 경로)
icons = {
    "상의": "https://img.icons8.com/fluency/96/t-shirt.png",
    "하의": "https://img.icons8.com/fluency/96/jeans.png",
    "신발": "https://img.icons8.com/fluency/96/sneakers.png",
    "가방": "https://img.icons8.com/fluency/96/handbag.png"
}

# 색상 박스 출력 함수
def color_box(label, color_name, icon_url):
    color = color_codes.get(color_name, "#FFFFFF")
    text_color = "#000000" if color_name != "블랙" else "#FFFFFF"
    st.markdown(
        f"""
        <div style="display:flex; align-items:center; margin:5px 0;">
            <img src="{icon_url}" width="40" style="margin-right:10px;">
            <div style="width:30px; height:30px; background-color:{color}; 
                        border:1px solid #000; margin-right:10px;"></div>
            <span style="color:{text_color}; font-weight:bold;">{label}: {color_name}</span>
        </div>
        """,
        unsafe_allow_html=True
    )

# 앱 시작
st.title("👗 옷 코디 전체 추천 앱")
st.write("상의 색을 선택하면 하의, 신발, 가방까지 풀 코디를 추천해드려요!")

# 사용자 입력
selected_top = st.selectbox("👕 상의 색을 골라주세요:", list(outfit_palette.keys()))

if st.button("✨ 코디 추천받기"):
    palette = outfit_palette[selected_top]
    bottom = random.choice(palette["하의"])
    shoes = random.choice(palette["신발"])
    bag = random.choice(palette["가방"])

    st.subheader("오늘의 추천 코디 ✨")

    color_box("👕 상의", selected_top, icons["상의"])
    color_box("👖 하의", bottom, icons["하의"])
    color_box("👟 신발", shoes, icons["신발"])
    color_box("👜 가방", bag, icons["가방"])

    st.info("👉 액세서리 아이콘도 추가하면 더 리얼하게 만들 수 있어요!")
