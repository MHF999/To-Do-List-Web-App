import streamlit as web
import functions

def add_todo():
    todo = web.session_state['new_todo']
    todos.append(todo)
    functions.write_todos(todos)

def remove_todo():
    for index, todo in enumerate(todos):
        if web.session_state[index]:
            todos.pop(index)
            functions.write_todos(todos)
            del web.session_state[index]


todos = functions.get_todos()

web.title("To-Do App")

for index, todo in enumerate(todos):
    web.checkbox(todo, on_change=remove_todo, key=index)

web.text_input(label="", placeholder="Enter a to-do...",
               on_change=add_todo, key='new_todo')