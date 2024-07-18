import streamlit as st
import functions


todos=functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo) 
    functions.write_todos(todos)





st.title("My Todo App")
st.subheader("This is My First Python App.")
st.write("This app will work, InshaAllah")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"todo_{index}")
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[f"todo_{index}"]
        st.experimental_rerun()



st.text_input(label='', placeholder= "Enter your new ToDo...",
              on_change=add_todo, key="new_todo")
