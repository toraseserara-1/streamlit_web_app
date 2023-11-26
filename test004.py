import streamlit as st
import numpy as np


st.title("Streamlit Text Example")

st.markdown("""
## 概要
このページは、テキスト表示機能の具体例を記述するものです。

### 構成
- [st.write](https://docs.streamlit.io/library/api-reference/write-magic/st.write): 色々表示できる
- [st.code](https://docs.streamlit.io/library/api-reference/text/st.code): シンタックスハイライトしたコードを表示できる
""")

st.write("数値: ", 2)
st.write("配列も表示可能: ", np.random.normal(size=5))

body = """
import numpy as np
a = np.random.normal(0, 1, size=500)
"""
st.code(body, language="python")


a = np.random.normal(0, 1, size=500)

st.code(a, language="python")