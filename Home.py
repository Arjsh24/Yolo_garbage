import streamlit as st

st.set_page_config(
    page_title='가비지타임',
    page_icon='🔥',
    layout='wide',
    initial_sidebar_state='auto'
)

st.header('가비지타임')

st.image('images/main.PNG')
st.write('')
st.text(' "헷갈리는 분리배출 완전정복" ')
st.divider()

st.subheader(':mag: 서비스 소개')
st.write('')
st.write('')
col1, col2 = st.columns(2)
col2.image('images/recycling.PNG')
col1.subheader('재활용품 분류기')
col1.divider()
col1.markdown('''재활용품 이미지를 업로드하면, 환경부 분리배출 기준에 따라 항목을 분류합니다.  
AI를 활용하여 한 이미지 안에 서로 다른 여러 물질이 있어도 모두 인식하여 분류할 수 있습니다.  
휴대폰으로 서비스 이용 시, 휴대폰 카메라로 재활용 사진을 촬영하여 실시간으로 분류해볼 수 있습니다.''')
col1.write('')
col1.link_button('바로가기', "https://hajinhw-final-home-smsg6m.streamlit.app/%EC%9E%AC%ED%99%9C%EC%9A%A9%ED%92%88_%EB%B6%84%EB%A5%98%EA%B8%B0")

st.write('')
st.write('')
col1, col2 = st.columns(2)
col2.image('images/guide.PNG')
col1.subheader('분리배출 가이드')
col1.divider()
col1.markdown('''재활용품 분리배출 가이드를 제공합니다.  
환경부 기준과 서울시 각 구청별 기준에 따라 각 항목별 분리배출 정보를 보여줍니다.
''')
col1.write('')
col1.link_button('바로가기', "https://hajinhw-final-home-smsg6m.streamlit.app/%EB%B6%84%EB%A6%AC%EB%B0%B0%EC%B6%9C_%EA%B0%80%EC%9D%B4%EB%93%9C")

st.divider()

st.subheader(':bulb: 왜 필요한가요?')
st.write('')
st.write('')
st.markdown(':heavy_check_mark: 잘못된 분리배출로 인해 :blue-background[환경 문제]가 발생합니다')

st.markdown('''- **유해성분 누출 위험**: 매립 및 소각되는 쓰레기의 증가로 인해 유해 성분이 누출될 위험 증가  
- **환경오염**: 쓰레기 증가로 인한 토양, 수질, 대기 오염 등 환경오염 문제  
- OECD 환경성과평가 기준 한국은 '재활용 모범국가’ 지만 (명목 재활용률 86.5%), 실질 재활용률은 22.7% 정도로 낮음''')
st.image('images/earth.PNG')

st.write('')
st.markdown(':heavy_check_mark: 분리배출 위반 시 :blue-background[과태료 부과]')
st.markdown('''- 분리배출 기준을 준수하지 않으면 과태료가 부과될 수 있습니다.  
- 투명 페트병을 유색 페트병 또는 일반 플라스틱과 함께 버리면 1차 적발 시 10만 원, 2차 적발 시 20만 원, 3차 적발 시 30만 원  
- 음식물 쓰레기나 플라스틱, 캔 등 재활용품을 분리배출 하지 않고 종량제 봉투에 섞어 버릴 경우에도 위와 동일  
- 일반 쓰레기를 종량제 봉투를 사용하지 않고 일반 비닐에 담아 버리면 적발 때마다 20만 원''')
st.text('※ 2024년 7월 환경부 기준으로, 추후 변경될 수 있으며 지자체에 따라 기준이 다를 수 있음')

st.write('')
st.markdown(':heavy_check_mark: :blue-background[글로벌] 시장 현황')
st.markdown('''- 원자재 가격 상승과 공급 불안정 속, 폐플라스틱 폐배터리 재생이용 에너지 회수 등 재활용 사업이 미래 성장동력으로 부상  
- 사용한 자원을 다시 원료로 순환시키는 이른바 '요람에서 요람으로' 발상이 핵심 대안 중 하나로 급부상  
- 제조업을 중심으로 폐플라스틱을 활용한 열분해유 추출 또는 회유금속 추출 등 투입된 자재를 재생이용하고 에너지화하는 재활용 사업을 미래 먹거리로 육성하려는 트렌드  ''')


st.write('')
st.write('')
st.markdown(':earth_asia: 올바른 분리배출로 과태료 피하고, 지구도 지킵시다!')
st.write('')
st.write('')
footer_html = """<div style='text-align: left;'>
  <p>© garbage time 2024</p>
</div>"""
st.markdown(footer_html, unsafe_allow_html=True)