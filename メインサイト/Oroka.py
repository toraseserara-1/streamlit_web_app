import streamlit as st

def main():
  st.title("oroka.py")

  if st.button("情報を表示する"):
    with open("Subject.txt","r") as file:
      user_date1 = file.read()
    st.write(user_data)
if __name__ == "__main__":
  main()
