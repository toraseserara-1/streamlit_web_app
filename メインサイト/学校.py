import streamlit as st 
from PIL import Image
import datetime


date = datetime.datetime.now()
date1 = (date.year)
date2 = (date.month)
date3 = (date.day)
date4 = (date.hour)
date5 = (date.minute)
date6 = (date.second)

st.title("提出物の日程登録フォーム")

image = Image.open("メインサイト/data/悩み君.png")
st.image(image,width=50)

with st.form(key='確認'):
    name = st.text_input("名前(任意です。)")
    
    subject = st.selectbox("教科選択",("選択してください","現代国語","言語文化","英語コミュニケーションI","論理表現I","数学I","情報数学I","公共","化学基礎","保健体育","体育（男子）","体育（女子）","情報産業と社会","芸術（書道）","芸術（美術）","芸術（音楽）","その他"))
    
    start_date = st.date_input("締め切り日",datetime.date(date1,date2,date3))
    
    hour = st.slider('何時までですか？', 0, 23, 12)
    minite = st.slider('何分までですか？', 0, 59, 30)
    second1 = st.slider('何秒までですか？', 0, 59, 30)
    content = st.text_area("内容（できるだけ短くお願いします。）")
    
    submit_btn = st.form_submit_button(label='決定')
    if submit_btn:
            st.text(name+"先生。予定が設定されました。ありがとうございます。")
        
     
    
if submit_btn:
    print(subject)
    print(start_date)
    print(str(hour)+"時"+str(minite)+'分'+str(second1)+"秒")
    print(content)