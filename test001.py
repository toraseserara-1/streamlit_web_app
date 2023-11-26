import streamlit as st

def main():
    # Markdownのdivタグとstyle属性を使用して左揃えにする
    st.markdown("""
        <div style="text-align: left;">
            <h1>Hello, Streamlit with Left Alignment!</h1>
        </div>
    """, unsafe_allow_html=True)

if __name__ == '__main__':
    main()

