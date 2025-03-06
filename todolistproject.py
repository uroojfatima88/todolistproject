import streamlit as st
import json


def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)


if "tasks" not in st.session_state:
    st.session_state.tasks = load_tasks()

st.title("📝 To-Do List ")


new_task = st.text_input("Enter a new task:")
if st.button("Add Task"):
    if new_task:
        st.session_state.tasks.append({"task": new_task, "completed": False})
        save_tasks(st.session_state.tasks)
        st.rerun()
    else:
        st.warning("Task cannot be empty!")



for index, task in enumerate(st.session_state.tasks):
    col1, col2 = st.columns([0.8, 0.2])
    with col1:
        task_completed = st.checkbox(task["task"], value=task["completed"], key=f"task_{index}")
        st.session_state.tasks[index]["completed"] = task_completed
    with col2:
        if st.button("delete task", key=f"del_{index}"):
            del st.session_state.tasks[index]
            save_tasks(st.session_state.tasks)
            st.rerun()


save_tasks(st.session_state.tasks)
