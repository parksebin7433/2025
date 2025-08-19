import streamlit as st
import random

# 계절 + 스타일별 색상 팔레트 (상의 → 나머지 아이템)
outfit_palette = {
    "봄": {
        "캐주얼": {
            "화이트": {
                "하의": ["데님 블루", "베이지"],
                "신발": ["화이트", "핑크"],
                "가방": ["브라운", "화이트"]
            },
            "핑크": {
                "하의": ["화이트", "그레이"],
                "신발": ["화이트", "블랙"],
                "가방": ["네이비", "화이트"]
            }
        },
        "포멀": {
            "베이지": {
                "하의": ["화이트", "네이비"],
                "신발": ["브라운", "블랙"],
                "가방": ["블랙", "브라운"]
            },
            "화이트": {
                "하의": ["블랙", "네이비"],
                "신발": ["블랙", "실버"],
                "가방": ["블랙", "네이비"]
            }
        },
        "스포츠": {
            "그레이": {
                "하의": ["블랙", "네이비"],
                "신발": ["화이트", "민트"],
                "가방": ["블랙", "그레이"]
            },
            "화이트": {
                "하의": ["블랙", "그레이"],
                "신발": ["화이트", "레드"],
                "가방": ["블랙", "화이트"]
            }
        }
    },
    "여름": {
        "캐주얼": {
            "화이트": {
                "하의": ["데님 블루", "네이비"],
                "신발": ["화이트", "블랙"],
                "가방": ["네이비", "화이트"]
            },
            "옐로우": {
                "하의": ["화이트", "네이비"],
                "신발": ["화이트", "베이지"],
                "가방": ["브라운", "화이트"]
            }
        },
        "포멀": {
            "네이비": {
                "하의": ["화이트", "그레이"],
                "신발": ["블랙", "브라운"],
                "가방": ["화이트", "브라운"]
            }
        },
        "스포츠": {
            "블랙": {
                "하의": ["그레이", "화이트"],
                "신발": ["블랙", "화이트"],
                "가방": ["화이트", "실버"]
            }
        }
    },
    # 👉 가을, 겨울도 필요하면 같은 방식으로 확장 가능
}

# HTML용 색상 코드 (미리보기용)
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

# 색상 박스 출력 함수
def color_box(label, color_name):
    color = color_codes.get(color_name, "#FFFFFF")
    text_color = "#000000" if color_name != "블랙" else "#FFFFFF"
    st.markdown(
        f"""
        <div style="display:flex; align-items:center; margin:5px 0;">
            <div style="width:30px; height:30px; background-color:{color}; 
                        border:1px solid #000; margin-right:10px;"></div>
            <span style="color:{text_color}; font-weight:bold;">{label}: {color_name}</span>
        </div>
        """,
        unsafe_allow_html=True
    )

# 앱 시작
st.title("👗 옷 코디 전체 추천 앱")
st.write("계절과 스타일을 선택하고, 상의 색을 고르면 하의·신발·가방까지 **3세트 코디**를 추천해드려요!")

# 사용자 입력
season = st.selectbox("🍂 계절을 선택해주세요:", list(outfit_palette.keys()))
style = st.selectbox("🎯 스타일을 선택해주세요:", list(outfit_palette[season].keys()))

# 선택된 시즌·스타일에 맞는 상의 색상만 보여주기
available_tops = list(outfit_palette[season][style].keys())
selected_top = st.selectbox("👕 상의 색을 골라주세요:", available_tops)

if st.button("✨ 코디 추천받기"):
    palette = outfit_palette[season][style][selected_top]

    st.subheader(f"{season} · {style} 스타일 추천 코디 3세트 ✨")

    for i in range(1, 3+1):
        bottom = random.choice(palette["하의"])
        shoes = random.choice(palette["신발"])
        bag = random.choice(palette["가방"])

        st.markdown(f"### 👗 코디 {i}")
        color_box("👕 상의", selected_top)
        color_box("👖 하의", bottom)
        color_box("👟 신발", shoes)
        color_box("👜 가방", bag)
        st.markdown("---")

    st.info("👉 계절·스타일에 맞는 색 조합으로 더 자연스러운 코디를 즐겨보세요!")
