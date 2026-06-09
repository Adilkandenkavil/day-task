from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

tasks = {}
next_id = 1



class TaskCreate(BaseModel):
    title: str
    description: str


class TaskUpdate(BaseModel):
    title: str
    description: str
    completed: bool


class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    completed: bool



@router.get("/", response_model=list[TaskResponse])
def get_tasks():
    return list(tasks.values())



@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(404, "Task not found")
    return tasks[task_id]



@router.post("/", response_model=TaskResponse, status_code=201)
def create_task(task: TaskCreate):
    global next_id

    new_task = {
        "id": next_id,
        "title": task.title,
        "description": task.description,
        "completed": False
    }

    tasks[next_id] = new_task
    next_id += 1

    return new_task


@router.put("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task: TaskUpdate):
    if task_id not in tasks:
        raise HTTPException(404, "Task not found")

    updated_task = {
        "id": task_id,
        "title": task.title,
        "description": task.description,
        "completed": task.completed
    }

    tasks[task_id] = updated_task
    return updated_task


@router.delete("/{task_id}")
def delete_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(404, "Task not found")

    del tasks[task_id]
    return {"message": "Task deleted"}



@router.patch("/{task_id}/complete", response_model=TaskResponse)
def complete_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(404, "Task not found")

    tasks[task_id]["completed"] = True
    return tasks[task_id]