import streamlit as st
import  functions

todos = functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("My to-do app.")
st.subheader("This is my to-do app.")
st.write("This app is to increase your productivity")

incrementor = 1
for todo in todos:
    st.checkbox(todo, key=incrementor)
    incrementor = incrementor + 1


st.text_input(label=" " ,placeholder="Add new to-do...",
              on_change=add_todo, key='new_todo')