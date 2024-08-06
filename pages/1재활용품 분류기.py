import streamlit as st
from ultralytics import YOLO
import cv2
import numpy as np

st.set_page_config(
    page_title='재활용품 분류기',
    page_icon='🔥',
    layout='wide',
    initial_sidebar_state='auto'
)

st.subheader('재활용품 분류기')
with st.container(border=False):
    st.info(''' AI를 활용하여 재활용품 항목을 분류합니다.  
    이미 저장된 이미지를 업로드하거나, 직접 실시간으로 사진을 찍어서 분류해볼 수 있습니다.''')

st.write('')
tab1, tab2 = st.tabs(['이미지 업로드', '사진 촬영'])

# 이미지 업로드
with tab1:
    model = YOLO('model/best.pt')  # 사전 학습된 모델 사용
    uploaded_file = st.file_uploader("이미지 파일을 등록해주세요", type=['png', 'jpg', 'jpeg'])
    col1, col2 = st.columns(2)

    if uploaded_file is not None:
        col1.image(uploaded_file)

        # 이미지를 OpenCV 형식으로 읽기
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, 1)

        # 모델로 예측 수행
        results = model(image)

        # 결과를 이미지에 그리기
        annotated_image = results[0].plot()

        # 결과 이미지 출력

        col2.image(annotated_image, channels="BGR", caption="재활용 분류 결과")

        clss = results[0].boxes.cls.tolist()
        clss_set = list(set(results[0].boxes.cls.tolist()))
        co_set = len(clss_set)
        conff = results[0].boxes.conf.tolist()
        co = len(clss)

        st.divider()
        st.subheader('인식 결과')
        st.markdown('')
        for i in range(co):
            if clss[i] == 0:
                st.write(f'{i+1}. :blue-background[종이팩] (약 {np.round(conff[i], 2) * 100} %)')
            if clss[i] == 1:
                st.write(f'{i+1}. :blue-background[종이컵] (약 {np.round(conff[i], 2) * 100} %)')
            if clss[i] == 2:
                st.write(f'{i+1}. :blue-background[종이컵+이물질] (약 {np.round(conff[i], 2) * 100} %)')
            if clss[i] == 3:
                st.write(f'{i+1}. :green-background[플라스틱] (약 {np.round(conff[i], 2) * 100} %)')
            if clss[i] == 4:
                st.write(f'{i+1}. :green-background[플라스틱+이물질] (약 {np.round(conff[i], 2) * 100} %)')
            if clss[i] == 5:
                st.write(f'{i+1}. :red-background[페트] (약 {np.round(conff[i], 2) * 100} %)')
            if clss[i] == 6:
                st.write(f'{i+1}. :red-background[페트+이물질] (약 {np.round(conff[i], 2) * 100} %)')
            if clss[i] == 7:
                st.write(f'{i+1}. :violet-background[페트+다중포장재] (약 {np.round(conff[i], 2) * 100} %)')
            if clss[i] == 8:
                st.write(f'{i+1}. :violet-background[페트+이물질+다중포장재] (약 {np.round(conff[i], 2) * 100} %)')


        st.divider()
        st.subheader('분류 가이드')
        st.markdown('')
        for i in range(co_set):
            if clss_set[i] == 0:
                st.write(f''':recycle: :blue-background[종이팩]    
                              
                            플라스틱 빨대 등이나 이물질이 없는지 다시 한번 확인하고 말려서 배출해 주세요.  
    강서구,성동구,금천구,강동구와 같이 주민센터 등에 전용수거함이 없는 경우 종이류와 섞이지 않게 묶어서 배출해 주세요.  
    노원구의 경우 종이컵과 통합배출합니다.   
    종이팩 분리배출과 관련하여 자세한 사항은 분리배츨 가이드 페이지를 참고해주세요!''')

            if clss_set[i] == 1:
                st.write(f''':recycle: :blue-background[종이컵]  
                  
                            이물질이 없는지 다시 한번 확인 후 종이컵으로 배출해 주세요.  
    종이류, 종이팩과 분리하여 배출합니다. 단, 노원구의 경우 종이팩과 통합배출합니다.  
    종이컵 분리배출과 관련하여 자세한 사항은 분리배츨 가이드 페이지를 참고해주세요!''')

            if clss_set[i] == 2:
                st.write(f''':recycle: :blue-background[종이컵+이물질]  
                
                            이물질이 묻어있는 종이컵으로 보입니다. 이물질 없이 깨끗이 씻은 후 말린 상태로 배출해 주세요.  
    만약 이물질 제거가 힘들다면, 일반쓰레기로 배출해 주세요.  
    종이컵 분리배출과 관련하여 자세한 사항은 분리배츨 가이드 페이지를 참고해주세요!''')

            if clss_set[i] == 3:
                st.write(f''':recycle: :green-background[플라스틱]  
                
                            혼합플라스틱 또는 타재료와 함께 배출할 수 없으며, 이물질이 없는지 다시 한 번 확인 후 배출해 주세요.  
    노원구의 경우 기판을 분리한 전화기 또는 금속부분을 분리한 장난감 등은 배출할 수 있습니다.  
    관악구와 서대문구는 노끈을 플라스틱/비닐 등 원재료에 따라 분리배출 가능합니다.  
    플라스틱 분리배출과 관련하여 자세한 사항은 분리배츨 가이드 페이지를 참고해주세요!''')

            if clss_set[i] == 4:
                st.write(f''':recycle: :green-background[플라스틱+이물질]  
                
                            이물질이 묻어있는 플라스틱으로 보입니다. 이물질 없이 깨끗이 씻은 후 배출해 주세요.  
    만약 이물질 제거가 힘들다면, 일반쓰레기로 배출해 주세요.  
    관악구와 서대문구는 노끈을 플라스틱/비닐 등 원재료에 따라 분리배출 가능합니다.   
    플라스틱 분리배출과 관련하여 자세한 사항은 분리배츨 가이드 페이지를 참고해주세요!''')

            if clss_set[i] == 5:
                st.write(f''':recycle: :red-background[페트]  
                 
                            이물질 또는 다른 재질은 없는지 확인 후 배출해 주세요.  
    가능한 색상별로 분리배출해 주시되, 유색페트병의 경우 종로구는 배출불가, 동대문구는 플라스틱류로 배출해 주세요.   
    은평구에서는 불투명한 페트병도 배출 불가능합니다.  
    페트 분리배출과 관련하여 자세한 사항은 분리배출 가이드 페이지를 참고해주세요!''')

            if clss_set[i] == 6:
                st.write(f''':recycle: :red-background[페트+이물질]  
                
                            이물질이 묻어있는 페트로 보입니다. 이물질 없이 깨끗이 씻은 후 배출해 주세요.  
    만약 이물질 제거가 힘들다면, 일반쓰레기로 배출해 주세요.  
    가능한 색상별로 분리배출해 주시되, 유색페트병의 경우 종로구는 배출불가, 동대문구는 플라스틱류로 배출해 주세요.   
    은평구에서는 불투명한 페트병도 배출 불가능합니다.  
    페트 분리배출과 관련하여 자세한 사항은 분리배출 가이드 페이지를 참고해주세요!''')

            if clss_set[i] == 7:
                st.write(f''':recycle: :violet-background[페트+다중포장재]  
                
                            다중포장재가 포함된 페트로 보입니다. 포장재를 제거한 후 배출해 주세요.  
    만약 포장재 제거가 힘들다면, 일반쓰레기로 배출해 주세요.  
    가능한 색상별로 분리배출해 주시되, 유색페트병의 경우 종로구는 배출불가, 동대문구는 플라스틱류로 배출해 주세요.   
    은평구에서는 불투명한 페트병도 배출 불가능합니다.  
    페트 분리배출과 관련하여 자세한 사항은 분리배출 가이드 페이지를 참고해주세요!''')

            if clss_set[i] == 8:
                st.write(f''':recycle: :violet-background[페트+이물질+다중포장재]  
                
                            이물질과 다중포장재가 포함된 페트로 보입니다. 이물질과 포장재를 제거한 후 배출해 주세요.  
    만약 제거가 힘들다면, 일반쓰레기로 배출해 주세요.  
    가능한 색상별로 분리배출해 주시되, 유색페트병의 경우 종로구는 배출불가, 동대문구는 플라스틱류로 배출해 주세요.   
    은평구에서는 불투명한 페트병도 배출 불가능합니다.  
    페트 분리배출과 관련하여 자세한 사항은 분리배출 가이드 페이지를 참고해주세요!''')

        st.write('')
        st.write('')
        st.link_button('분리배출 가이드',
                       "http://localhost:8501/%EB%B6%84%EB%A6%AC%EB%B0%B0%EC%B6%9C_%EA%B0%80%EC%9D%B4%EB%93%9C")
        st.write('')
        st.write('')
        st.write(':bulb: 2024년 8월 환경부 기준으로 분류한 것이며, 추후 변경될 수 있습니다.')
        st.write(':bulb: 인식 결과는 실제와 차이가 있을 수 있습니다.')




# 사진 촬영
with tab2:
    picture = st.camera_input("사진을 찍어주세요")
    model = YOLO('model/best.pt')
    if picture:

        # 이미지를 OpenCV 형식으로 읽기
        file_bytes = np.asarray(bytearray(picture.read()), dtype=np.uint8)
        image2 = cv2.imdecode(file_bytes, 1)

        # 모델로 예측 수행
        results2 = model(image2)

        # 결과를 이미지에 그리기
        annotated_image2 = results2[0].plot()

        # 결과 이미지 출력
        st.text('')
        st.image(annotated_image2, channels="BGR", caption="재활용 분류 결과")

        st.markdown('')
        clss2 = results2[0].boxes.cls.tolist()
        clss_set2 = list(set(results2[0].boxes.cls.tolist()))
        co_set2 = len(clss_set2)
        conff2 = results2[0].boxes.conf.tolist()
        co2 = len(clss2)

        st.divider()
        st.subheader('인식 결과')
        st.markdown('')
        for i in range(co2):
            if clss2[i] == 0:
                st.write(f'{i + 1}. :blue-background[종이팩] (약 {np.round(conff[i], 2) * 100} %)')
            if clss2[i] == 1:
                st.write(f'{i + 1}. :blue-background[종이컵] (약 {np.round(conff[i], 2) * 100} %)')
            if clss2[i] == 2:
                st.write(f'{i + 1}. :blue-background[종이컵+이물질] (약 {np.round(conff[i], 2) * 100} %)')
            if clss2[i] == 3:
                st.write(f'{i + 1}. :green-background[플라스틱] (약 {np.round(conff[i], 2) * 100} %)')
            if clss2[i] == 4:
                st.write(f'{i + 1}. :green-background[플라스틱+이물질] (약 {np.round(conff[i], 2) * 100} %)')
            if clss2[i] == 5:
                st.write(f'{i + 1}. :red-background[페트] (약 {np.round(conff[i], 2) * 100} %)')
            if clss2[i] == 6:
                st.write(f'{i + 1}. :red-background[페트+이물질] (약 {np.round(conff[i], 2) * 100} %)')
            if clss2[i] == 7:
                st.write(f'{i + 1}. :violet-background[페트+다중포장재] (약 {np.round(conff[i], 2) * 100} %)')
            if clss2[i] == 8:
                st.write(f'{i + 1}. :violet-background[페트+이물질+다중포장재] (약 {np.round(conff[i], 2) * 100} %)')

        st.divider()
        st.subheader('분류 가이드')
        st.markdown('')
        for i in range(co_set2):
            if clss_set2[i] == 0:
                st.write(f''':recycle: :blue-background[종이팩]    

                            플라스틱 빨대 등이나 이물질이 없는지 다시 한번 확인하고 말려서 배출해 주세요.  
    강서구,성동구,금천구,강동구와 같이 주민센터 등에 전용수거함이 없는 경우 종이류와 섞이지 않게 묶어서 배출해 주세요.  
    노원구의 경우 종이컵과 통합배출합니다.   
    종이팩 분리배출과 관련하여 자세한 사항은 분리배츨 가이드 페이지를 참고해주세요!''')

            if clss_set2[i] == 1:
                st.write(f''':recycle: :blue-background[종이컵]  

                            이물질이 없는지 다시 한번 확인 후 종이컵으로 배출해 주세요.  
    종이류, 종이팩과 분리하여 배출합니다. 단, 노원구의 경우 종이팩과 통합배출합니다.  
    종이컵 분리배출과 관련하여 자세한 사항은 분리배츨 가이드 페이지를 참고해주세요!''')

            if clss_set2[i] == 2:
                st.write(f''':recycle: :blue-background[종이컵+이물질]  

                                이물질이 묻어있는 종이컵으로 보입니다. 이물질 없이 깨끗이 씻은 후 말린 상태로 배출해 주세요.  
        만약 이물질 제거가 힘들다면, 일반쓰레기로 배출해 주세요.  
        종이컵 분리배출과 관련하여 자세한 사항은 분리배츨 가이드 페이지를 참고해주세요!''')

            if clss_set2[i] == 3:
                st.write(f''':recycle: :green-background[플라스틱]  

                            혼합플라스틱 또는 타재료와 함께 배출할 수 없으며, 이물질이 없는지 다시 한 번 확인 후 배출해 주세요.  
    노원구의 경우 기판을 분리한 전화기 또는 금속부분을 분리한 장난감 등은 배출할 수 있습니다.  
    관악구와 서대문구는 노끈을 플라스틱/비닐 등 원재료에 따라 분리배출 가능합니다.  
    플라스틱 분리배출과 관련하여 자세한 사항은 분리배츨 가이드 페이지를 참고해주세요!''')

            if clss_set2[i] == 4:
                st.write(f''':recycle: :green-background[플라스틱+이물질]  

                            이물질이 묻어있는 플라스틱으로 보입니다. 이물질 없이 깨끗이 씻은 후 배출해 주세요.  
    만약 이물질 제거가 힘들다면, 일반쓰레기로 배출해 주세요.  
    관악구와 서대문구는 노끈을 플라스틱/비닐 등 원재료에 따라 분리배출 가능합니다.   
    플라스틱 분리배출과 관련하여 자세한 사항은 분리배츨 가이드 페이지를 참고해주세요!''')

            if clss_set2[i] == 5:
                st.write(f''':recycle: :red-background[페트]  

                            이물질 또는 다른 재질은 없는지 확인 후 배출해 주세요.  
    가능한 색상별로 분리배출해 주시되, 유색페트병의 경우 종로구는 배출불가, 동대문구는 플라스틱류로 배출해 주세요.   
    은평구에서는 불투명한 페트병도 배출 불가능합니다.  
    페트 분리배출과 관련하여 자세한 사항은 분리배출 가이드 페이지를 참고해주세요!''')

            if clss_set2[i] == 6:
                st.write(f''':recycle: :red-background[페트+이물질]  

                            이물질이 묻어있는 페트로 보입니다. 이물질 없이 깨끗이 씻은 후 배출해 주세요.  
    만약 이물질 제거가 힘들다면, 일반쓰레기로 배출해 주세요.  
    가능한 색상별로 분리배출해 주시되, 유색페트병의 경우 종로구는 배출불가, 동대문구는 플라스틱류로 배출해 주세요.   
    은평구에서는 불투명한 페트병도 배출 불가능합니다.  
    페트 분리배출과 관련하여 자세한 사항은 분리배출 가이드 페이지를 참고해주세요!''')

            if clss_set2[i] == 7:
                st.write(f''':recycle: :violet-background[페트+다중포장재]  

                            다중포장재가 포함된 페트로 보입니다. 포장재를 제거한 후 배출해 주세요.  
    만약 포장재 제거가 힘들다면, 일반쓰레기로 배출해 주세요.  
    가능한 색상별로 분리배출해 주시되, 유색페트병의 경우 종로구는 배출불가, 동대문구는 플라스틱류로 배출해 주세요.   
    은평구에서는 불투명한 페트병도 배출 불가능합니다.  
    페트 분리배출과 관련하여 자세한 사항은 분리배출 가이드 페이지를 참고해주세요!''')

            if clss_set2[i] == 8:
                st.write(f''':recycle: :violet-background[페트+이물질+다중포장재]  

                            이물질과 다중포장재가 포함된 페트로 보입니다. 이물질과 포장재를 제거한 후 배출해 주세요.  
    만약 제거가 힘들다면, 일반쓰레기로 배출해 주세요.  
    가능한 색상별로 분리배출해 주시되, 유색페트병의 경우 종로구는 배출불가, 동대문구는 플라스틱류로 배출해 주세요.   
    은평구에서는 불투명한 페트병도 배출 불가능합니다.  
    g페트 분리배출과 관련하여 자세한 사항은 분리배출 가이드 페이지를 참고해주세요!''')

        st.write('')
        st.write('')
        st.link_button('분리배출 가이드',
                       "http://localhost:8501/%EB%B6%84%EB%A6%AC%EB%B0%B0%EC%B6%9C_%EA%B0%80%EC%9D%B4%EB%93%9C")
        st.write('')
        st.write('')
        st.write(':bulb: 2024년 8월 환경부 기준으로 분류한 것이며, 추후 변경될 수 있습니다.')
        st.write(':bulb: 인식 결과는 실제와 차이가 있을 수 있습니다.')

