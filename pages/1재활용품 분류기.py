import streamlit as st
import onnxruntime as ort
from PIL import Image
import numpy as np

st.set_page_config(
    page_title='재활용품 분류기',
    page_icon='🔥',
    layout='wide',
    initial_sidebar_state='auto'
)

# ✅ ONNX 모델 로드
@st.cache_resource
def load_model():
    return ort.InferenceSession("model/best.onnx")

session = load_model()

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
# 예측 함수
# -----------------------------------
def predict(image):
    img = image.resize((640, 640))
    img = np.array(img) / 255.0
    img = img.transpose(2, 0, 1)
    img = np.expand_dims(img, axis=0).astype(np.float32)

    input_name = session.get_inputs()[0].name
    outputs = session.run(None, {input_name: img})

    return outputs

# -----------------------------------
# 결과 표시 함수
# -----------------------------------
def show_results(image):
    outputs = predict(image)

    st.image(image, caption="입력 이미지", use_container_width=True)

    predictions = outputs[0][0]  # (13, 8400)

    # confidence 값 기준으로 최고값 찾기
    confidences = predictions[4]
    best_idx = np.argmax(confidences)
    best_conf = confidences[best_idx]

    if best_conf < 0.5:
        st.warning("인식된 객체가 없습니다.")
        return

    class_scores = predictions[5:, best_idx]
    best_class = np.argmax(class_scores)

    label = labels.get(int(best_class), "알 수 없음")
    conf_percent = round(float(best_conf) * 100, 2)

    st.divider()
    st.subheader('인식 결과')
    st.write(f"{label} (약 {conf_percent} %)")

    st.divider()
    st.info("※ 인식 결과는 실제와 차이가 있을 수 있습니다.")

# -----------------------------------
# 이미지 업로드
# -----------------------------------
with tab1:
    uploaded_file = st.file_uploader("이미지 파일을 등록해주세요", type=['png', 'jpg', 'jpeg'])

    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert("RGB")
        show_results(image)

# -----------------------------------
# 사진 촬영
# -----------------------------------
with tab2:
    picture = st.camera_input("사진을 찍어주세요")

    if picture:
        image = Image.open(picture).convert("RGB")
        show_results(image)

# -----------------------------------
# 하단 안내
# -----------------------------------
st.divider()
st.link_button('분리배출 가이드', "/분리배출_가이드")
st.write(':bulb: 2024년 8월 환경부 기준이며 추후 변경될 수 있습니다.')
