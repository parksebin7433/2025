import streamlit as st
import random

# 여행지 리스트 (이모티콘 포함)
destinations = [
    "🏯 서울 - 경복궁 🏮🍵",
    "🏖️ 부산 - 해운대 🌊🦀",
    "🏝️ 제주 - 성산일출봉 🌋🍊",
    "🌅 강릉 - 경포대 🐟☕",
    "🏘️ 전주 - 한옥마을 🍲🥟",
    "🌉 여수 - 돌산대교 🦑🍶",
    "⛰️ 속초 - 설악산 🥔🦞",
    "🛕 경주 - 불국사 📜🍵",
    "🏮 인천 - 차이나타운 🥡🥟",
    "⛰️ 대구 - 팔공산 🌸🍜"
]

# 제목
st.title("🎯 랜덤 여행지 추천기 ✈️")

# 설명
st.write("🗺️ 버튼을 눌러 오늘의 랜덤 여행지를 추천받아보세요! 😍")

# 버튼 클릭 시 랜덤 여행지 추천
if st.button("🎁 여행지 추천받기"):
    selected = random.choice(destinations)
    st.success(f"✨ 오늘의 추천 여행지: **{selected}** 🎉")
