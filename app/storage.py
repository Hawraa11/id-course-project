from datetime import datetime, timezone, date
from typing import Optional

from app.models import TaskCreate, TaskResponse, TaskUpdate


_tasks: dict[str, TaskResponse] = {}


def add_task(payload: TaskCreate) -> TaskResponse:
    task_id = str(len(_tasks) + 1)
    now = datetime.now(timezone.utc)
    task = TaskResponse(
        id=task_id,
        title=payload.title,
        description=payload.description or "",
        status=payload.status,
        priority=payload.priority,
        assignee=payload.assignee,
        due_date=payload.due_date,
        created_at=now,
        updated_at=now,
    )
    _tasks[task_id] = task
    return task


def get_all_tasks(
    status: Optional[str] = None,
    priority: Optional[str] = None,
    search: Optional[str] = None,
    assignee: Optional[str] = None,
    overdue: Optional[bool] = None
) -> list[TaskResponse]:
    tasks = list(_tasks.values())
    if status:
        tasks = [t for t in tasks if t.status.value == status]
    if priority:
        tasks = [t for t in tasks if t.priority.value == priority]
    if search:
        search_term = search.strip().lower()
        tasks = [t for t in tasks if search_term in t.title.lower() or search_term in t.description.lower()]
    if assignee:
        assignee_term = assignee.strip().lower()
        tasks = [t for t in tasks if t.assignee and assignee_term in t.assignee.lower()]
    if overdue:
        today = date.today()
        tasks = [t for t in tasks if t.due_date and t.due_date < today and t.status.value != "Done"]
    return tasks


def get_task_by_id(task_id: str) -> Optional[TaskResponse]:
    return _tasks.get(task_id)


def update_task(task_id: str, payload: TaskUpdate) -> Optional[TaskResponse]:
    task = _tasks.get(task_id)
    if not task:
        return None
    update_data = payload.model_dump(exclude_unset=True)
    update_data["updated_at"] = datetime.now(timezone.utc)
    updated_task = task.model_copy(update=update_data)
    _tasks[task_id] = updated_task
    return updated_task


def delete_task(task_id: str) -> bool:
    if task_id in _tasks:
        del _tasks[task_id]
        return True
    return False


def _reset() -> None:
    _tasks.clear()
