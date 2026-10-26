from typing import Dict, List, Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Task API")


class TaskInput(BaseModel):
    title: str = Field(min_length=1)
    completed: bool = False


class Task(TaskInput):
    id: int


class TaskUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=1)
    completed: Optional[bool] = None


tasks: Dict[int, Task] = {}
next_task_id = 1


@app.get("/health")
def health_check():
    # TODO: Retorne o estado da API.
    pass


@app.get("/tasks", response_model=List[Task])
def list_tasks():
    # TODO: Retorne todas as tarefas.
    pass


@app.post("/tasks", response_model=Task, status_code=201)
def create_task(task_input: TaskInput):
    # TODO: Crie uma tarefa com um identificador único.
    pass


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    # TODO: Consulte a tarefa ou retorne HTTP 404.
    pass


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task_update: TaskUpdate):
    # TODO: Atualize a tarefa ou retorne HTTP 404.
    pass


@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    # TODO: Remova a tarefa ou retorne HTTP 404.
    pass