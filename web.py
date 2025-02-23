import streamlit as st
from streamlit import session_state

import functions

# Reading file
todos = functions.read_file()

def add_todo():
    if session_state["new_todo"] != "" and not session_state["new_todo"].isspace():
        local_todo = st.session_state["new_todo"] + "\n"
        todos.append(local_todo)
        functions.write_file(todos)
        st.session_state["new_todo"] = ""

def delete_todo():
    try:
        todos.pop(selected_index)
        functions.write_file(todos)
    except NameError:
        st.error("There's no item selected")

def edit_todo():
    if session_state["new_todo"] != "" and not session_state["new_todo"].isspace():
        local_todo = st.session_state["new_todo"] + "\n"
        todos[selected_index] = local_todo
        functions.write_file(todos)
        st.session_state["new_todo"] = ""

st.title("My To-Do App")
st.subheader("It's time to improve your productivity!")
st.write("Check your todos:")

marked_indexes = []

todo_options = [todo.strip() for todo in todos]
selected_todo = st.radio("", todo_options)

if selected_todo:
    selected_index = todo_options.index(selected_todo)
    # st.write(f"Selected index: {selected_index}")

# for index, todo in enumerate(todos):
#     checkbox = st.checkbox(todo, key=index)
#     if checkbox:
#         marked_indexes.append(index)

st.text_input(label="", placeholder="Enter a todo...", key="new_todo")
left, mid, right = st.columns(3)
left.button("Add", on_click=add_todo, type="primary", use_container_width=True)
mid.button("Complete", on_click=delete_todo, use_container_width=True)
right.button("Edit", on_click=edit_todo, use_container_width=True)


# st.session_state For debug