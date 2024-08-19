import streamlit as st
import base64
from PIL import Image
import wordcloud
page = st.sidebar.radio('我的网页',['答题','词典','留言区','图片处理','词云图'])
def ask(lesson,answer,a,b,c):
    # question = st.radio(lesson,['请选择','A','B','C'],captions=['',a,b,c])
    st.write(lesson)
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        cb3 = st.checkbox(a)
    with col2:
        cb4 = st.checkbox(b)
    with col3:
        cb5 = st.checkbox(c)
    if cb3:
        if cb4 or cb5:
            st.write('这是单选题，请选择仅一个选项')
        if cb3 and answer == 'A'or cb4 and answer == 'B'or cb5 and answer == 'C':
            st.write('正确')
        elif cb3 == False and cb4 == False and cb5 == False:
            pass
        else:
            st.write('错误')
    elif cb4 and cb5:
        st.write('这是单选题，请选择仅一个选项')
    else:
        if cb3 and answer == 'A'or cb4 and answer == 'B'or cb5 and answer == 'C':
            st.write('正确')
        elif cb3 == False and cb4 == False and cb5 == False:
            pass
        else:
            st.write('错误')
    st.write('')
    st.write('')
def ciyun(str):
    font = "anna.ttf"
    w = wordcloud.WordCloud(width=600, height=400,font_path=font, max_words=50).generate(str)
    w.to_file("ciyun.png")
    img = Image.open("ciyun.png")
    return img
def page_bg(img):
    last = 'jpg'
    st.markdown(f"""<style>.stApp {{background: url(data:img/{last};base64,{base64.b64encode(open(img, 'rb').read()).decode()});
        background-size: cover}}</style>""",unsafe_allow_html = True,)
# page_bg('天象奇景.jpg')

def page_1():
    ques = [['铜砝码能浮在？','C','水中','盐水中','水银中'],
            ['太阳属于哪一类星体？','B','行星','恒星','卫星'],
            ['地球有几颗卫星？','B','0','1','2'],
            ['哪颗行星能浮在水上？','C','木星','火星','土星'],
            ['成年人身体里有几块骨头？','A','206','133','312'],
            ['中国的英文缩写是？','B','CHI','CHN','CHA'],
            ['赵州桥是哪个朝代修建的？','A','隋朝','唐朝','宋朝'],
            ['以下哪项是化学变化？','A','木炭燃烧','水结冰','气球爆炸'],
            ['我国最早的成熟文字是？','C','小篆','草书','甲骨文'],
            ['最早使用小数的国家是？','B','埃及','中国','希腊'],
            
            ['下面哪个图形不是四边形','C','梯形','长方形','扇形'],
            ['碳的化学符号是？','A','C','O','S'],
            ['相邻两个时区的时差是几个小时？','B','0.5','1','2'],
            ['太阳占太阳系百分之多少的质量？','C','71.3%','98.6%','99.8%'],
            ['最亮的星星是那颗？','B','北极星','天狼星','织女星'],
            ['气候的两个重要因素是？','A','气温，降水','气温，气压','风力，气压'],
            ['太阳最终会变成什么？','B','黑洞','白矮星','中子星'],
            ['死海属于那种水域？','B','海洋','湖泊','河流'],
            ['除太阳以外，离我们最近的恒星是？','A','比邻星','北极星','冥王星'],
            ['中国处于亚洲的哪里？','A','东亚','南亚','东南亚'],
            ['亚洲唯一的发达国家是？','B','中国','日本','韩国'],
            ['没有人定居的大洲是哪个洲？','C','欧洲','非洲','南极洲'],
            ['中国面积最大的岛是？','A','台湾岛','海南岛','钓鱼岛'],
            ['以下哪种数据类型属于图片？','A','png','txt','MP3'],
            ['以下哪项不会发光？','B','太阳','月亮','萤火虫'],
            ['企鹅生活在哪里 ？','A','南极','北极','大洋洲'],
            ['哪颗行星有漂亮的光环？','C','火星','木星','土星'],
            ['使用频率最高的字母是哪个？','B','a','e','t'],
            ['在农历的哪天有可能看到月食？','C','初一','初八','十五'],
            ['人体最小的骨头在哪里？','C','手部','腿部','耳朵'],
            ['以下哪种物质具有腐蚀性？','A','消毒液','煤炭','油'],
            ['撞击木星的彗星是哪颗？','C','百武彗星','哈雷彗星','苏梅克·列维9号']]
            # ['','','','',''],
            # ['','','','',''],
            # ['','','','',''],
            # ['','','','',''],
            # ['','','','',''],
            # ['','','','',''],
            # ['','','','',''],
            # ['','','','',''],
            # ['','','','',''],
            # ['','','','',''],
            # ['','','','',''],
            # ['','','','',''],
            # ['','','','',''],
            # ['','','','',''],
            # ['','','','',''],
            # ['','','','',''],
            # ['','','','',''],
            # ['','','','','']]
    st.write('每道题只有一个正确答案')
    start,end = st.slider('要显示第几题？',1,30,(1,30))
    for i in range(start-1,end):
        ask(ques[i][0],ques[i][1],ques[i][2],ques[i][3],ques[i][4])
def page_2():
    tab1,tab2 = st.tabs(['英文字典','中文字典'])
    with tab1:
        with open('words_space.txt', 'r', encoding='utf-8') as f:
            words_list = f.read().split('\n')
        for i in range(len(words_list)):
            words_list[i] = words_list[i].split('#')
        words_dict = {}
        for i in words_list:
            words_dict[i[1]] = [int(i[0]), i[2]]
        with open('check_out_times.txt', 'r', encoding='utf-8') as f:
            times_list = f.read().split('\n')
        for i in range(len(times_list)):
            times_list[i] = times_list[i].split('#')
        times_dict = {}
        for i in times_list:
            times_dict[int(i[0])] = int(i[1])
        word = st.text_input('请输入要查询的单词')
        if word in words_dict:
            st.write(words_dict[word])
            n = words_dict[word][0]
            if n in times_dict:
                times_dict[n] += 1
            else:
                times_dict[n] = 1
            with open('check_out_times.txt', 'w', encoding='utf-8') as f:
                message = ''
                for k, v in times_dict.items():
                    message += str(k) + '#' + str(v) + '\n'
                message = message[:-1]
                f.write(message)
            st.write('查询次数：', times_dict[n])
    with tab2:
        pass
def page_3():
    with open('leave_messages.txt', 'r', encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    for i in messages_list:
        if i[1] == '编程猫':
            with st.chat_message('💯'):
                st.write(i[1],':',i[2])
        elif i[1] == '阿短':
            with st.chat_message('🍥'):
                st.write(i[1],':',i[2])
    name = st.selectbox('我是____', ['阿短', '编程猫'])
    new_message = st.text_input('想要说的话____')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
        with open('leave_messages.txt', 'w', encoding='utf-8') as f:
            message = ''
            for i in messages_list:
                message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)
def img_change(img,rc,gc,bc):
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x, y] = (b, g, r)
    return img
def page_4():
    st.write(":sunglasses:图片换色小程序:sunglasses:")
    uploaded_file = st.file_uploader("上传帅图", type=['png', 'jpeg', 'jpg'])
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        tab1,tab2,tab3,tab4 = st.tabs(["原图","改色1","改色2","改色3"])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img, 0, 2, 1))
        with tab3:
            st.image(img_change(img, 1, 0, 1))
        with tab4:
            st.image(img_change(img, 2, 2, 0))
def page_5():
    uploaded_file = st.file_uploader("上传txt文件")
    if uploaded_file is not None:
        str_data = uploaded_file.read().decode("utf-8")
        st.image(ciyun(str_data))
    else:
        pass
if page == '答题':
    page_1()
if page == '词典':
    page_2()
if page == '留言区':
    page_3()
if page == '图片处理':
    page_4()
if page == '词云图':
    page_5()
