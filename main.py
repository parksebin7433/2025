import streamlit as st
import folium
from streamlit_folium import st_folium
import random

# -------------------
# 장소 예시 데이터 (임시)
# -------------------
sample_places = [
    {"name": "관광지 1", "lat": 37.5665, "lon": 126.9780, "desc": "유명한 관광 명소"},
    {"name": "관광지 2", "lat": 37.5700, "lon": 126.9920, "desc": "전통 시장"},
    {"name": "관광지 3", "lat": 37.5651, "lon": 126.9895, "desc": "역사 박물관"},
    {"name": "관광지 4", "lat": 37.5711, "lon": 126.9769, "desc": "전망 좋은 공원"},
    {"name": "관광지 5", "lat": 37.5670, "lon": 126.9820, "desc": "맛집 거리"},
]

# -------------------
# 페이지 제목
# -------------------
st.set_page_config(page_title="여행 일정 자동 생성기", layout="wide")
st.title("🗺 여행 일정 자동 생성기")

# -------------------
# 입력 받기
# -------------------
destination = st.text_input("여행지 입력", placeholder="예: 서울, 부산, 제주")
days = st.number_input("여행 기간 (일)", min_value=1, max_value=30, value=3)
budget = st.number_input("예산 (₩)", min_value=0, step=10000, value=300000)

if st.button("일정 생성"):
    if not destination:
        st.warning("여행지를 입력하세요.")
    else:
        st.subheader(f"📅 {destination} {days}일 여행 일정")
        itinerary = []

        # 예시 일정 생성 (랜덤 장소 선택)
        for day in range(1, days+1):
            morning = random.choice(sample_places)
            afternoon = random.choice([p for p in sample_places if p != morning])
            itinerary.append({
                "day": day,
                "morning": morning,
                "afternoon": afternoon
            })

        # 일정 표 출력
        for day_plan in itinerary:
            st.markdown(f"### Day {day_plan['day']}")
            st.write(f"**오전**: {day_plan['morning']['name']} - {day_plan['morning']['desc']}")
            st.write(f"**오후**: {day_plan['afternoon']['name']} - {day_plan['afternoon']['desc']}")
            st.write("---")

        # 지도 생성
        m = folium.Map(location=[sample_places[0]["lat"], sample_places[0]["lon"]], zoom_start=13)
        for day_plan in itinerary:
            folium.Marker(
                [day_plan['morning']["lat"], day_plan['morning']["lon"]],
                popup=f"Day {day_plan['day']} 오전: {day_plan['morning']['name']}"
            ).add_to(m)
            folium.Marker(
                [day_plan['afternoon']["lat"], day_plan['afternoon']["lon"]],
                popup=f"Day {day_plan['day']} 오후: {day_plan['afternoon']['name']}"
            ).add_to(m)

        st_folium(m, width=700, height=500)
