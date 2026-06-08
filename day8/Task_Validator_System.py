from typing import Optional
from pydantic import BaseModel, EmailStr, ValidationError
import json
import requests


class UserModel(BaseModel):
    name: str
    email: EmailStr
    age: int


class TaskModel(BaseModel):
    title: str
    description: Optional[str] = None
    priority: str
    completed: bool = False


def create_task(data: dict) -> TaskModel:
    return TaskModel(**data)


def tasks_to_json(tasks: list[TaskModel]) -> str:
    return json.dumps(
        [task.model_dump() for task in tasks],
        indent=4
    )

class TodoResponse(BaseModel):
    userId: int
    id: int
    title: str
    completed: bool

def fetch_todo(todo_id: int) -> TodoResponse:
    response = requests.get(
        f"https://jsonplaceholder.typicode.com/todos/{todo_id}"
    )

    response.raise_for_status()

    data = response.json()

    return TodoResponse(**data)

tasks = []

try:
    task1 = create_task({
        "title": "Learn Pydantic",
        "description": "Practice validation",
        "priority": "High"
    })

    task2 = create_task({
        "title": "Build FastAPI App",
        "priority": "Medium"
    })

    tasks.extend([task1, task2])

    print("Tasks created successfully\n")

except ValidationError as e:
    print(e.errors()[0]["msg"])


try:
    json_data = tasks_to_json(tasks)

    print("JSON Output:")
    print(json_data)

except Exception as e:
    print(str(e))


try:
    todo = fetch_todo(1)

    print("\nAPI Response Parsed:")
    print(todo)

except ValidationError as e:
    print(e.errors()[0]["msg"])

except requests.RequestException as e:
    print(str(e))