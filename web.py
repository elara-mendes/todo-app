import streamlit as st
import functions

# Reading file
todos = functions.read_file()

def add_todo():
    local_todo = st.session_state["new_todo"] + "\n"
    todos.append(local_todo)
    functions.write_file(todos)
    st.session_state["new_todo"] = ""

st.title("My To-Do App")
st.subheader("It's time to improve your productivity!")
st.write("Check your todos:")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=index)
    if checkbox:
        todos.pop(index)
        functions.write_file(todos)
        st.rerun()

st.text_input(label="", placeholder="Enter a todo...", on_change=add_todo, key="new_todo")


# st.session_state