import streamlit as st
x = st.slider("Select a value")
st.write(x, "squared is", x * x)

#st.sidebar.text_input("文字入力欄") #引数に入力内容を渡せる
st.sidebar.text_area("テキストエリア")