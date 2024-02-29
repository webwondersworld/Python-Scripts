from datetime import datetime
from plyer import notification
import threading
import time
import sys

# File to store tasks
TASK_FILE = "tasks.txt"


# Function to load tasks from file
def load_tasks():
    tasks = []
    try:
        with open(TASK_FILE, "r") as file:
            for line in file:
                parts = line.strip().split(";")
                name = parts[0]
                due_datetime = datetime.strptime(parts[1], "%Y-%m-%d %H:%M:%S")
                notification_sent = True if parts[2].lower() == 'true' else False
                completed = True if parts[3].lower() == 'true' else False

                tasks.append({
                    "name": name,
                    "due_datetime": due_datetime,
                    "notification_sent": notification_sent,
                    "completed": completed
                })
    except FileNotFoundError:
        pass
    return tasks


# Function to save tasks to file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(
                f"{task['name']};{task['due_datetime'].strftime('%Y-%m-%d %H:%M:%S')};{task['notification_sent']};{task['completed']}\n")


# Function to check for due tasks and send notifications
def check_due_tasks(tasks):
    while True:
        current_time = datetime.now()
        for task in tasks:
            if not task['notification_sent'] and not task['completed'] and task['due_datetime'] <= current_time:
                notification_text = f"Task '{task['name']}' is due now!"
                notification.notify(
                    title="Task Manager",
                    message=notification_text,
                    app_name="Task Manager",
                    timeout=10
                )
                task['notification_sent'] = True  # Mark notification as sent
                save_tasks(tasks)
        time.sleep(60)  # Check every 60 seconds for due tasks


# Function to add a new task
def add_task(tasks):
    task_name = input("Enter Task Name: ")
    due_datetime_str = input("Enter Due Date and Time (YYYY-MM-DD HH:MM): ")
    due_datetime = datetime.strptime(due_datetime_str, "%Y-%m-%d %H:%M")

    tasks.append({"name": task_name, "due_datetime": due_datetime, "notification_sent": False, "completed": False})
    save_tasks(tasks)
    print("Task added successfully.")


# Function to mark a task as completed
def complete_task(tasks):
    open_tasks = [task for task in tasks if not task['completed']]
    if open_tasks:
        print("Open Tasks:")
        for i, task in enumerate(open_tasks, start=1):
            print(f"{i}. {task['name']} - Due Date: {task['due_datetime'].strftime('%Y-%m-%d %H:%M')}")

        task_index = int(input("Enter the index of the task to mark as complete: ")) - 1
        if 0 <= task_index < len(open_tasks):
            tasks[tasks.index(open_tasks[task_index])]['completed'] = True
            save_tasks(tasks)
            print(f"Task '{open_tasks[task_index]['name']}' marked as completed.")
        else:
            print("Invalid task index.")
    else:
        print("No open tasks.")


# Function to delete a task
def delete_task(tasks):
    task_index = int(input("Enter the index of the task to delete: ")) - 1
    if 0 <= task_index < len(tasks):
        del tasks[task_index]
        save_tasks(tasks)
        print("Task deleted successfully.")
    else:
        print("Invalid task index.")


# Function to view open tasks
def view_open_tasks(tasks):
    open_tasks = [task for task in tasks if not task['completed']]
    print("Open Tasks:")
    if open_tasks:
        for i, task in enumerate(open_tasks, start=1):
            print(f"{i}. {task['name']} - Due Date: {task['due_datetime'].strftime('%Y-%m-%d %H:%M')}")
    else:
        print("No open tasks.")


# Function to view completed tasks
def view_completed_tasks(tasks):
    completed_tasks = [task for task in tasks if task['completed']]
    print("Completed Tasks:")
    if completed_tasks:
        for i, task in enumerate(completed_tasks, start=1):
            print(f"{i}. {task['name']} - Due Date: {task['due_datetime'].strftime('%Y-%m-%d %H:%M')}")
    else:
        print("No completed tasks.")


# Load tasks from file
tasks = load_tasks()

# Create and start the thread for checking due tasks
check_due_tasks_thread = threading.Thread(target=check_due_tasks, args=(tasks,))
check_due_tasks_thread.start()

while True:
    print("\nOptions:")
    print("1. Add Task")
    print("2. Complete Task")
    print("3. View Open Tasks")
    print("4. View Completed Tasks")
    print("5. Exit")

    option = input("Enter your choice: ")

    if option == '1':
        add_task(tasks)
    elif option == '2':
        complete_task(tasks)
    elif option == '3':
        view_open_tasks(tasks)
    elif option == '4':
        view_completed_tasks(tasks)
    elif option == '5':
        sys.exit()
    else:
        print("Invalid option.")

# Join the thread for checking due tasks
check_due_tasks_thread.join()
