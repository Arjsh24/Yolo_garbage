import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np

st.set_page_config(
    page_title='재활용품 분류기',
    page_icon='🔥',
    layout='wide',
    initial_sidebar_state='auto'
)

# ✅ 모델은 한 번만 로드
@st.cache_resource
def load_model():
    return YOLO("model/best.pt")

model = load_model()

st.subheader('재활용품 분류기')

with st.container(border=False):
    st.info(''' AI를 활용하여 재활용품 항목을 분류합니다.  
이미 저장된 이미지를 업로드하거나, 직접 실시간으로 사진을 찍어서 분류해볼 수 있습니다.''')

st.write('')
tab1, tab2 = st.tabs(['이미지 업로드', '사진 촬영'])


# -----------------------------------
# 라벨 정의
# -----------------------------------
labels = {
    0: "종이팩",
    1: "종이컵",
    2: "종이컵+이물질",
    3: "플라스틱",
    4: "플라스틱+이물질",
    5: "페트",
    6: "페트+이물질",
    7: "페트+다중포장재",
    8: "페트+이물질+다중포장재"
}


# -----------------------------------
# 결과 출력 함수
# -----------------------------------
def show_results(results):
    result = results[0]

    # 박스 그려진 이미지 표시
    annotated_image = result.plot()
    st.image(annotated_image, caption="재활용 분류 결과")

    if result.boxes is None or len(result.boxes) == 0:
        st.warning("인식된 객체가 없습니다.")
        return

    classes = result.boxes.cls.tolist()
    confidences = result.boxes.conf.tolist()

    st.divider()
    st.subheader('인식 결과')

    for i, cls in enumerate(classes):
        conf_percent = round(confidences[i] * 100, 2)
        label = labels.get(int(cls), "알 수 없음")
        st.write(f"{i+1}. {label} (약 {conf_percent} %)")

    st.divider()
    st.info("※ 인식 결과는 실제와 차이가 있을 수 있습니다.")


# -----------------------------------
# 이미지 업로드
# -----------------------------------
with tab1:
    uploaded_file = st.file_uploader("이미지 파일을 등록해주세요", type=['png', 'jpg', 'jpeg'])

    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, caption="업로드 이미지")

        results = model.predict(image, conf=0.5)
        show_results(results)


# -----------------------------------
# 사진 촬영
# -----------------------------------
with tab2:
    picture = st.camera_input("사진을 찍어주세요")

    if picture:
        image = Image.open(picture).convert("RGB")
        st.image(image, caption="촬영 이미지")

        results = model.predict(image, conf=0.5)
        show_results(results)


# -----------------------------------
# 하단 안내
# -----------------------------------
st.divider()
st.link_button('분리배출 가이드', "/분리배출_가이드")
st.write(':bulb: 2024년 8월 환경부 기준이며 추후 변경될 수 있습니다.')
