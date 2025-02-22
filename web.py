import streamlit as st
import functions

todos = functions.read_file()

st.title("My To-Do App")
st.subheader("It's time to improve your productivity!")
st.write("Check your todos:")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Enter a todo...")