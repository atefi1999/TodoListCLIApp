import os


class Task:
    def __init__(self, id, title, completed=False):
        self.id = id
        self.title = title
        self.completed = completed

    def mark_done(self):
        self.completed = True

    def __str__(self):
        status = "✅" if self.completed else "❌"
        return f"{self.id}. {self.title} [{status}]"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        task_id = len(self.tasks) + 1
        task = Task(task_id, title)
        self.tasks.append(task)
        return task

    def remove_task(self, id):
        self.tasks = [t for t in self.tasks if t.id != id]
        # Re-number IDs after removal
        for i, task in enumerate(self.tasks, start=1):
            task.id = i

    def list_tasks(self):
        return self.tasks

    def get_task(self, id):
        for task in self.tasks:
            if task.id == id:
                return task
        return None

    def mark_task_done(self, id):
        task = self.get_task(id)
        if task:
            task.mark_done()
            return True
        return False


class FileHandler:
    def __init__(self, filename="tasks.txt"):
        self.filename = filename

    def save(self, tasks):
        with open(self.filename, "w", encoding="utf-8") as f:
            for task in tasks:
                line = f"{task.id}|{task.title}|{task.completed}\n"
                f.write(line)

    def load(self):
        tasks = []
        if not os.path.exists(self.filename):
            return tasks
        with open(self.filename, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) == 3:
                    task_id, title, completed = parts
                    tasks.append(Task(int(task_id), title, completed == "True"))
        return tasks


class TodoCLI:
    def __init__(self):
        self.manager = TaskManager()
        self.file_handler = FileHandler()
        # Load saved tasks
        self.manager.tasks = self.file_handler.load()

    def show_menu(self):
        print("\n📋 Todo List Menu")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Done")
        print("4. Remove Task")
        print("5. Save & Exit")

    def handle_input(self, choice):
        if choice == "1":
            title = input("Enter task title: ")
            task = self.manager.add_task(title)
            print(f"✅ Task added: {task}")
        elif choice == "2":
            tasks = self.manager.list_tasks()
            if not tasks:
                print("⚠️ No tasks found.")
            else:
                for task in tasks:
                    print(task)
        elif choice == "3":
            task_id = int(input("Enter task ID to mark as done: "))
            if self.manager.mark_task_done(task_id):
                print("✅ Task marked as done.")
            else:
                print("⚠️ Task not found.")
        elif choice == "4":
            task_id = int(input("Enter task ID to remove: "))
            self.manager.remove_task(task_id)
            print("🗑️ Task removed.")
        elif choice == "5":
            self.file_handler.save(self.manager.tasks)
            print("💾 Tasks saved. Goodbye!")
            return False
        return True

    def run(self):
        print("🚀 Welcome to Todo List CLI App")
        running = True
        while running:
            self.show_menu()
            choice = input("Choose an option: ")
            running = self.handle_input(choice)


# ---------------- Sample Run ----------------
if __name__ == "__main__":
    app = TodoCLI()
    app.run()
