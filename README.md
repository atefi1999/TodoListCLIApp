# 📋 Todo List CLI App

A simple **Command-Line Interface (CLI) Todo List application** built with Python.  
Manage tasks easily: add, list, mark as done, remove, and save your tasks locally.

---

## 🧩 Features

- Add new tasks with a title.
- List all tasks with their status (done/pending).
- Mark tasks as done.
- Remove tasks.
- Persistent storage with a local file (`tasks.txt`).
- Simple and intuitive CLI interface.

---

## 🏗️ Technologies Used

- Python 3
- `os` module (for file handling)

---


## 📝 Classes & OOP Map

```backtick
**Task**
- `__init__(self, id, title, completed=False)` → Initialize a task
- `mark_done()` → Mark task as done
- `__str__()` → String representation of task

**TaskManager**
- `add_task(title)` → Add a new task
- `remove_task(id)` → Remove a task
- `list_tasks()` → Return list of all tasks
- `get_task(id)` → Get task by ID
- `mark_task_done(id)` → Mark task as done

**FileHandler**
- `save(tasks)` → Save tasks to file
- `load()` → Load tasks from file

**TodoCLI**
- `show_menu()` → Display CLI menu
- `handle_input(choice)` → Handle user input
- `run()` → Run the CLI application loop
```
---

## 🚀 How to Run

#### 1. Clone the repository:

```bash
git clone https://github.com/atefi1999/TodoListCLIApp.git
cd TodoListCLIApp
```

#### 2. Run the app:

```bash
python todo_list_cli_app.py
```
---
## 🎮 Sample Run
```backtick
🚀 Welcome to Todo List CLI App

📋 Todo List Menu
1. Add Task
2. List Tasks
3. Mark Task as Done
4. Remove Task
5. Save & Exit

Choose an option: 1
Enter task title: Finish Python project
✅ Task added: 1. Finish Python project [❌]

Choose an option: 2
1. Finish Python project [❌]

Choose an option: 3
Enter task ID to mark as done: 1
✅ Task marked as done.

Choose an option: 2
1. Finish Python project [✅]

Choose an option: 5
💾 Tasks saved. Goodbye!
```
---
## 📂 Notes

- Tasks are automatically saved to tasks.txt.
- Task IDs are re-numbered after removal to keep the list consistent.
- CLI interface is user-friendly and intuitive

---

## 🗂️ Project Structure
```markdown
.
├── todo_cli.py # Main CLI program
├── tasks.txt # File storing tasks (auto-created)
└── README.md # Project documentation
```
