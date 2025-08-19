import streamlit as st
import random

# 기본 색상 팔레트와 조합
color_combinations = {
    "흰색": ["검정", "데님 블루", "베이지", "카키"],
    "검정": ["흰색", "그레이", "레드", "라벤더"],
    "베이지": ["화이트", "브라운", "네이비", "블랙"],
    "네이비": ["화이트", "베이지", "옐로우", "그레이"],
    "회색": ["블랙", "화이트", "핑크", "민트"],
    "빨강": ["블랙", "화이트", "데님", "네이비"],
    "초록": ["화이트", "베이지", "브라운", "블랙"],
    "노랑": ["화이트", "네이비", "블랙", "베이지"],
    "핑크": ["화이트", "그레이", "네이비", "블랙"],
}

st.title("👗 옷 색 조합 추천 앱")

st.write("상의 색을 선택하면 어울리는 하의/아우터 색상을 추천해드립니다!")

# 사용자 입력
selected_color = st.selectbox("상의 색을 골라주세요:", list(color_combinations.keys()))

if st.button("추천받기"):
    suggestions = random.sample(color_combinations[selected_color], 2)
    st.success(f"💡 '{selected_color}' 상의에는 이런 색이 잘 어울려요: {', '.join(suggestions)}")

    st.write("👉 코디할 때는 신발이나 가방 같은 포인트 컬러도 추가하면 좋아요!")

