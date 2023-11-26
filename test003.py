import streamlit as st

numbers = [1,2,3,4,5,6,7,8,9]
text = ""
for i in numbers:
  if i%2==0:
    text += f'<span style="color:coral">{i}</span>'
  else:
    text += f'<span style="color:darkgray">{i}</span>'        

st.markdown('**color change example:**\n') #太字
st.markdown("---") #区切り線
st.write(text, unsafe_allow_html=True)
