import streamlit as st 
from PIL import Image
import datetime
import test005

st.title("提出物の日程登録フォーム")

image = Image.open("悩み君.png")
st.image(image, width=50)

# メインのフォーム
with st.form(key='main_form'):
    name = st.text_input("名前（任意です。）")
    subject = st.selectbox("教科選択", ("選択してください", "現代国語", "言語文化", "英語コミュニケーションI", "論理表現I", "数学I", "情報数学I", "公共", "化学基礎", "保健体育", "体育（男子）", "体育（女子）", "情報産業と社会", "芸術（書道）", "芸術（美術）", "芸術（音楽）", "その他"))
    start_date = st.date_input("締め切り日", datetime.date(test005.date1, test005.date2, test005.date3))
    hour = st.slider('何時までですか？', 0, 23, 12)
    minute = st.slider('何分までですか？', 0, 59, 30)
    second1 = st.slider('何秒までですか？', 0, 59, 30)
    content = st.text_area("内容（できるだけ短くお願いします。）")

    # フォームのボタン
    submit_btn = st.form_submit_button(label='確認')

# フォームが送信されたときの処理
if submit_btn:
    # 確認セクション
    st.write("確認セクション")
    st.text("教科:", str(subject))
    st.text("締め切り日程:", str(start_date))
    st.text("締め切り時間:", f"{hour}時{minute}分{second1}秒")
    st.text("内容:", str(content))
    st.text("確認します")

    # 確認セクションのボタン
    submit_btn1 = st.form_submit_button(label='確認')

    # 確認セクションのボタンが押されたときの処理
    if submit_btn1:
        st.text(f"{name}先生。予定が設定されました。ありがとうございます。")
