import streamlit as st

st.set_page_config(
    page_title='분리배출 가이드',
    page_icon='🔥',
    layout='wide',
    initial_sidebar_state='auto'
)

st.subheader('분리배출 가이드')
with st.container(border=False):
    st.info('''환경부 기준과 서울시 각 구청별 기준에 따라 각 항목별 분리배출 정보를 보여줍니다.  
    ※ 2024년 8월 기준 정책이며, 추후 내용이 변경될 수 있습니다.''')

st.write('')
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs(['고철류', '금속캔', '비닐', '스티로폼', '유리병',
                                                                '종이류', '종이팩', '페트병', '플라스틱'])

# 고철류
with tab1:
    st.write('')
    col1, col2, col3 = st.columns([1,3,4], vertical_alignment="center")
    col1.write('''고철   
    비철금속''')
    col2.image('images/fe.png')
    # col1.write('')
    col3.markdown(':black_small_square: 이물질이 섞이지 않도록 한 후 봉투에 넣거나 끈으로 묶어서 배출')

    st.divider()
    st.write(''':o: 해당품목  
    공기구, 철사, 못 등 고철류  
    알루미늄, 스테인리스 제품 등 비철금속류''')
    st.write(''':x: 비해당품목  
    금속 이외의 재질(천, 고무, 플라스틱 등)이 부착된 우산, 프라이팬, 전기용품 등  
    **재질별로 분리가 곤란한 경우** 종량제봉투, 특수규격마대 또는 대형폐기물 처리 등 지자체 조례에 따라 배출''')

    st.divider()
    st.write(':exclamation: 재질별로 분리가 곤란한 경우')
    st.markdown(''':black_small_square: **우산**  
    재질별 분리 불가시 종량제봉투로 배출  
    :blue-background[관악구], :orange-background[서대문구] : 분리가 어려우면 고철로 배출''')

    st.markdown(''':black_small_square: **송곳**  
    재질별 분리 불가시 종량제봉투로 배출''')

# 금속캔
with tab2:
    st.write('')
    col1, col2, col3 = st.columns([1, 2, 4], vertical_alignment="center")
    col1.markdown('철캔/알루미늄캔')
    col2.image('images/can.PNG')
    col3.write(''':black_small_square: 내용물을 비우고 물로 헹구는 등 이물질을 제거하여 배출  
    :black_small_square: 담배꽁초 등 이물질을 넣지 않고 배출  
    :black_small_square: 플라스틱 뚜껑 등 금속캔과 다른 재질은 제거한 후 배출''')
    col3.write(''':o: 해당품목  
    음료수캔, 맥주캔, 통조림캔 등''')
    col3.write(''':x: 비해당품목  
    알루미늄 호일 등 (* 종량제 봉투로 배출)''')

    st.divider()
    col1, col2, col3 = st.columns([1, 2, 4], vertical_alignment="center")
    col1.markdown('''부탄가스  
    살충제용기''')
    col2.image('images/gas.PNG')
    col3.write(''':black_small_square: 내용물을 제거한 후 배출   
    :black_small_square: 가스용기는 내용물을 완전히 제거한 후 배출''')
    col3.write(''':o: 해당품목  
    부탄가스 용기, 살충제 용기, 스프레이 용기 등''')

    st.divider()
    col1, col2, col3 = st.columns([1.5, 1.5, 4], vertical_alignment="center")
    col1.markdown('내용물이 남아있는 캔류(락카, 페인트통 등)')
    col2.image('images/roc.png')
    col3.write(''':black_small_square: :blue-background[구로구]: 페인트/오일 등 담았던 캔 제외  
    :black_small_square: :orange-background[마포구]: 페인트, 오일, 유해성물질포장통 제외  
    :black_small_square: :green-background[강서구]: 특수규격마대에 담아 배출''')

# 비닐
with tab3:
    st.write('')
    col1, col2, col3 = st.columns([1, 2, 5], vertical_alignment="center")
    col1.markdown('''비닐포장재  
    1회용 비닐봉투''')
    col2.image('images/vinyl.PNG')
    col3.write(''':black_small_square: PET, PVC, PE, PP, PS, PSP 재질 등의 용기·트레이류  
    :black_small_square: 내용물을 비우고 물로 헹구는 등 이물질을 제거하여 배출   
    :black_small_square: 흩날리지 않도록 봉투에 담아 배출''')
    col3.write(''':o: 해당품목  
    1회용 봉투 등 각종 비닐류  
    분리배출표시가 없는 비닐류 포함''')
    col3.write(''':x: 비해당품목  
    깨끗하게 이물질 제거가 되지 않은 랩필름 등   
    식탁보, 고무장갑, 장판, 돗자리, 섬유류 등(천막, 현수막, 의류, 침구류 등)  
    ※ 종량제봉투, 특수규격마대 또는 대형폐기물 처리 등 지자체 조례에 따라 배출''')
    col3.write('')
    col3.write(''':black_small_square: **노끈**  
    :blue-background[관악구], :orange-background[서대문구], :green-background[금천구] : 플라스틱 또는 비닐로 재질에 따라 배출''')

# 스티로폼
with tab4:
    st.write('')
    col1, col2, col3 = st.columns([1, 2, 5], vertical_alignment="center")
    col1.markdown('''스티로폼  
    완충재''')
    col2.image('images/sti.PNG')
    col3.write(''':black_small_square: 내용물을 비우고 물로 헹구는 등 이물질을 제거하여 배출  
    :black_small_square: 부착상표 등 스티로폼과 다른 재질은 제거한 후 배출       
    :black_small_square: TV 등 전자제품 구입 시 완충재로 사용되는 발포합성수지 포장재는 가급적 구입처로 반납  
    :blue-background[노원구] : 재활용 배출가능''')
    st.divider()
    st.write(''':o: 해당품목  
    농·수·축산물 포장용 발포스티렌상자, 전자제품 완충재로 사용되는 발포합성수지포장재    
    :orange-background[강동구] : 농수축산물포장재 등도 구입처로 반납  
    :green-background[마포구] : 과일류 낱개포장 불가''')
    st.write(''':x: 비해당품목  
    타 재질과 코팅 또는 접착된 발포스티렌, 건축용 내·외장재 스티로폼, 이물질을 제거하기 어려운 경우 등      
    ※ 종량제봉투, 특수규격마대 또는 대형폐기물 처리 등 지자체 조례에 따라 배출''')
    st.write(''':black_small_square: **유색/코팅된 스티로폼**  
    :red-background[강남구] : PP봉투 이용  
    :gray-background[중랑구] : 동사무소, 공동주택 등 수거함이 설치되어 있는 장소에 배출''')

# 유리병
with tab5:
    st.write('')
    col1, col2, col3 = st.columns([1, 2, 4], vertical_alignment="center")
    col1.markdown('유리병류')
    col2.image('images/crystal.PNG')
    col3.write(''':black_small_square: 내용물을 비우고 물로 헹구는 등 이물질을 제거하여 배출  
    :black_small_square: 유리병이 깨지지 않도록 주의하여 배출  
    :black_small_square: 소주, 맥주 등 빈용기보증금 대상 유리병은 소매점 등으로 반납하여 보증금 환급  
    :black_small_square: 색상별 용기가 설치되어 색상별로 배출이 가능한 경우 분리배출''')
    col3.write(''':blue-background[중구] : 병뚜껑 제거 후 배출  
    :orange-background[종로구] : 화장품 유리병, 링거병 불가  
    :green-background[동대문구], :red-background[마포구] : 농약병 별도 배출''')
    st.divider()
    st.write(''':o: 해당품목  
    음료수병, 와인병, 양주병, 드링크병 등''')
    st.write(''':x: 비해당품목  
    깨진 유리제품: 신문지 등에 싸서 종량제 봉투 배출  
    코팅 및 다양한 색상이 들어간 유리제품, 내열 유리제품, 크리스탈 유리제품, 판유리, 조명기구용 유리류, 사기·도자기류 등  
    ※ 특수규격마대 또는 대형폐기물 처리 등 지자체 조례에 따라 배출''')

# 종이류
with tab6:
    st.write('')
    col1, col2, col3 = st.columns([1,1,5], vertical_alignment="center")
    col1.markdown('신문')
    col2.image('images/newspaper.PNG')
    col3.write(':black_small_square: 물기에 젖지 않도록 하고, 흩날리지 않도록 묶어서 배출')
    col3.write(''':x: 비해당품목  
    비닐 코팅 종이(광고지, 치킨 속포장재 등), 금박·은박지, 벽지, 자석전단지, 이물질을 제거하기 어려운 경우 등''')

    st.divider()
    col1, col2, col3 = st.columns([1,1,5], vertical_alignment="center")
    col1.markdown('책자/노트')
    col2.image('images/book.PNG')
    col3.write(':black_small_square: 스프링 등 종이류와 다른 재질은 제거한 후 배출')
    col3.write(''':o: 해당품목  
    책, 잡지, 공책, 노트 등''')
    col3.write(''':x: 비해당품목  
    비닐 코팅된 표지, 공책의 스프링 등은 제거한 후 배출(비닐포장지는 제외)  
    ※ 부속 재질에 따라 분리배출하거나 종량제봉투 등으로 배출''')

    st.divider()
    col1, col2, col3 = st.columns([1, 1, 5], vertical_alignment="center")
    col1.markdown('상자류')
    col2.image('images/box.PNG')
    col3.write(':black_small_square: 테이프 등 종이류와 다른 재질은 제거한 후 배출')
    col3.write(''':o: 해당품목  
    종이박스, 골판지 등''')
    col3.write(''':x: 비해당품목  
    비닐코팅 부분, 상자에 붙어있는 테이프, 철핀 등  
    ※ 부속 재질에 따라 분리배출하거나 종량제봉투 등으로 배출''')

    st.divider()
    st.markdown(':star: **종이류로 배출하면 안되는 품목** :star:')
    st.write('')
    col1, col2, col3 = st.columns(3)
    col1.image('images/notpaper1.PNG')
    col2.image('images/notpaper2.PNG')
    col3.image('images/notpaper3.PNG')
    col3.write(':blue-background[강남구] : 컵라면 용기는 세척 후 종이류로 배출 가능')

# 종이팩
with tab7:
    st.write('')
    col1, col2, col3 = st.columns([1, 1, 5], vertical_alignment="center")
    col1.markdown('종이팩')
    col2.image('images/pack.PNG')
    col3.write(''':black_small_square: 내용물을 비우고 물로 헹구는 등 이물질을 제거하고 말린 후 배출  
        :black_small_square: 빨대, 비닐 등 종이팩과 다른 재질은 제거한 후 배출  
        :black_small_square: 종이팩 전용수거함이 없는 경우에는 종이류와 구분할 수 있도록 가급적 끈 등으로 묶어 종이류 수거함으로 배출''')
    col3.write(''':o: 해당품목  
        우유팩, 두유팩, 소주팩, 쥬스팩 등''')
    col3.write(''':x: 비해당품목  
        종이류, 종이컵 등 (종이류 수거함으로 배출)''')
    st.write('')
    st.write('')
    st.image('images/pack_guide.PNG')

# 페트병
with tab8:
    st.write('')
    col1, col2, col3 = st.columns([1, 2, 4], vertical_alignment="center")
    col1.markdown('페트')
    col2.image('images/pet.PNG')
    col3.write(''':black_small_square: 내용물을 비우고 물로 헹구는 등 이물질을 제거하여 배출  
    :black_small_square: 부착상표, 부속품 등 본체와 다른 재질은 제거  
    :black_small_square: 압착하여 뚜껑을 닫아 배출  
    :black_small_square: :blue-background[송파구] : 종량제봉투 교환가능(각 동 주민센터)''')
    col3.image('images/label.PNG')

    st.divider()
    st.write(''':o: 해당품목  
    음료, 생수에 사용된 투명 페트병''')
    st.write(''':x: 비해당품목  
    1회용 컵, 식용유, 워셔액 등 용기 (일반 플라스틱류로 배출)''')

# 플라스틱
with tab9:
    st.write('')
    col1, col2, col3 = st.columns([0.5, 1, 4], vertical_alignment="center")
    col1.markdown('플라스틱')
    col2.image('images/plastic.PNG')
    col3.write(''':black_small_square: 내용물을 비우고 물로 헹구는 등 이물질을 제거하여 배출  
    :black_small_square: 물로 헹굴 수 없는 구조의 용기류(치약용기 등)는 내용물을 비운 후 배출   
    :black_small_square: 부착상표, 부속품 등 본체와 다른 재질은 제거한 후 배출''')

    st.divider()
    st.write(''':o: 해당품목  
    음료용기, 세정용기 등''')
    st.write(''':x: 비해당품목  
    :black_small_square: **플라스틱 이외의 재질이 부착된 경우**  
    완구·문구류, 옷걸이, 칫솔, 파일철, 전화기, 낚싯대, 유모차·보행기, CD·DVD 등  
    종량제봉투, 특수규격마대 또는 대형폐기물 처리 등 지자체 조례에 따라 배출  
    :blue-background[관악구], :orange-background[서대문구] : CD, 비디오/오디오 테이프는 플라스틱으로 배출, 필름(일반쓰레기) 분리 불가시 종량제봉투에 배출''')
    st.write(''':black_small_square: **혼합플라스틱(고무대야 등)**  
    :green-background[구로구]: 분리배출 가능(열에 녹지 않는 열경화성 플라스틱류 제외)  
    :red-background[노원구] : 바가지, 장난감(금속분리), 전화기(내부기판 제외) 가능  
    :blue-background[관악구], :orange-background[서대문구] : 고무대야 불가, 화분 불가''')
