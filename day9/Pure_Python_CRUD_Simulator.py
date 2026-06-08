from typing import Dict, List
class TaskError(Exception):
    pass
class TaskNotFoundError(TaskError):
    pass
class InvalidTaskDataError(TaskError):
    pass
tasks: Dict[int, dict] = {}
next_id: int = 1
def get_all_tasks() -> List[dict]:
    return list(tasks.values())
def get_task(task_id: int) -> dict:
    if task_id not in tasks:
        raise TaskNotFoundError("Task not found")
    return tasks[task_id]
def create_task(data: dict) -> dict:
    global next_id
    if "title" not in data or not data["title"]:
        raise InvalidTaskDataError("Title is required")
    task = {
        "id": next_id,
        "title": data["title"],
        "completed": data.get("completed", False)
    }
    tasks[next_id] = task
    next_id += 1
    return task
def update_task(task_id: int, data: dict) -> dict:
    if task_id not in tasks:
        raise TaskNotFoundError("Task not found")
    task = tasks[task_id]
    if "title" in data:
        task["title"] = data["title"]
    if "completed" in data:
        task["completed"] = data["completed"]
    return task
def delete_task(task_id: int) -> bool:
    if task_id not in tasks:
        raise TaskNotFoundError("Task not found")
    del tasks[task_id]
    return True
def menu() -> None:
    while True:
        print("\n--- TASK MANAGER ---")
        print("1. Create Task")
        print("2. View All Tasks")
        print("3. View One Task")
        print("4. Update Task")
        print("5. Delete Task")
        print("6. Exit")
        choice = input("Choose: ")
        try:
            if choice == "1":
                title = input("Task title: ")

                task = create_task({
                    "title": title
                })
                print("Created:", task)
            elif choice == "2":
                all_tasks = get_all_tasks()
                if not all_tasks:
                    print("No tasks found")
                else:
                    for task in all_tasks:
                        print(task)
            elif choice == "3":
                task_id = int(input("Task ID: "))
                print(get_task(task_id))
            elif choice == "4":
                task_id = int(input("Task ID: "))
                title = input("New title: ")
                completed = input("Completed (y/n): ").lower()
                updated_task = update_task(
                    task_id,
                    {
                        "title": title,
                        "completed": completed == "y"
                    }
                )
                print("Updated:", updated_task)
            elif choice == "5":
                task_id = int(input("Task ID: "))
                delete_task(task_id)
                print("Task deleted")
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice")
        except TaskError as e:
            print("Error:", e)
        except ValueError:
            print("Please enter a valid number")
if __name__ == "__main__":
    menu()