from datetime import date, timedelta
from app.models import TaskStatus, TaskPriority


def test_create_task_valid_returns_201_with_full_body(client):
    response = client.post("/tasks", json={"title": "Test Task"})
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test Task"
    assert data["status"] == "ToDo"
    assert data["priority"] == "Medium"
    assert "id" in data
    assert "created_at" in data
    assert "updated_at" in data


def test_create_task_missing_title_returns_422(client):
    response = client.post("/tasks", json={})
    assert response.status_code == 422


def test_create_task_blank_title_returns_422(client):
    response = client.post("/tasks", json={"title": "   "})
    assert response.status_code == 422


def test_create_task_null_title_returns_422(client):
    response = client.post("/tasks", json={"title": None})
    assert response.status_code == 422


def test_create_task_invalid_priority_returns_422(client):
    response = client.post("/tasks", json={"title": "Test", "priority": "Invalid"})
    assert response.status_code == 422


def test_create_task_unknown_field_returns_422(client):
    response = client.post("/tasks", json={"title": "Test", "unknown": "field"})
    assert response.status_code == 422


def test_list_tasks_empty_returns_200_and_empty_list(client):
    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.json() == []


def test_list_tasks_filter_by_status_no_match_returns_200_and_empty_list(client):
    response = client.get("/tasks?status=Done")
    assert response.status_code == 200
    assert response.json() == []


def test_list_tasks_filter_by_priority_returns_only_matches(client, created_task):
    client.post("/tasks", json={"title": "Low Task", "priority": "Low"})
    client.post("/tasks", json={"title": "High Task", "priority": "High"})
    
    response = client.get("/tasks?priority=High")
    assert response.status_code == 200
    tasks = response.json()
    assert len(tasks) == 1
    assert tasks[0]["priority"] == "High"


def test_get_task_by_id_returns_task(client, created_task):
    response = client.get(f"/tasks/{created_task['id']}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == created_task["id"]
    assert data["title"] == "fixture task"


def test_get_task_by_id_not_found_returns_404_with_detail(client):
    response = client.get("/tasks/999")
    assert response.status_code == 404
    assert "not found" in response.json()["detail"]


def test_patch_partial_update_keeps_other_fields(client, created_task):
    response = client.patch(f"/tasks/{created_task['id']}", json={"title": "Updated Title"})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated Title"
    assert data["status"] == created_task["status"]
    assert data["priority"] == created_task["priority"]


def test_patch_not_found_returns_404(client):
    response = client.patch("/tasks/999", json={"title": "Updated"})
    assert response.status_code == 404
    assert "not found" in response.json()["detail"]


def test_patch_valid_transition_todo_to_inprogress_returns_200(client, created_task):
    response = client.patch(f"/tasks/{created_task['id']}", json={"status": "InProgress"})
    assert response.status_code == 200
    assert response.json()["status"] == "InProgress"


def test_patch_invalid_transition_todo_to_done_returns_422(client, created_task):
    response = client.patch(f"/tasks/{created_task['id']}", json={"status": "Done"})
    assert response.status_code == 422
    assert "Invalid status transition" in response.json()["detail"]


def test_patch_same_status_returns_422(client, created_task):
    response = client.patch(f"/tasks/{created_task['id']}", json={"status": "ToDo"})
    assert response.status_code == 422
    assert "Invalid status transition" in response.json()["detail"]


def test_patch_null_title_returns_422(client, created_task):
    response = client.patch(f"/tasks/{created_task['id']}", json={"title": None})
    assert response.status_code == 422
    errors = response.json()["detail"]
    assert any("title cannot be null" in error.get("msg", "") for error in errors)


def test_delete_existing_returns_204_no_body(client, created_task):
    response = client.delete(f"/tasks/{created_task['id']}")
    assert response.status_code == 204
    assert response.content == b""


def test_delete_missing_returns_404(client):
    response = client.delete("/tasks/999")
    assert response.status_code == 404
    assert "not found" in response.json()["detail"]


def test_search_title_returns_matching_tasks(client):
    client.post("/tasks", json={"title": "Write report", "description": "Monthly report"})
    client.post("/tasks", json={"title": "Fix bug", "description": "Critical bug"})
    
    response = client.get("/tasks?search=report")
    assert response.status_code == 200
    tasks = response.json()
    assert len(tasks) == 1
    assert "report" in tasks[0]["title"].lower()


def test_search_description_returns_matching_tasks(client):
    client.post("/tasks", json={"title": "Task A", "description": "This is about testing"})
    client.post("/tasks", json={"title": "Task B", "description": "Something else"})
    
    response = client.get("/tasks?search=testing")
    assert response.status_code == 200
    tasks = response.json()
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Task A"


def test_search_case_insensitive(client):
    client.post("/tasks", json={"title": "Write REPORT", "description": "Important"})
    
    response = client.get("/tasks?search=report")
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_search_trims_whitespace(client):
    client.post("/tasks", json={"title": "Test task", "description": "Testing"})
    
    response = client.get("/tasks?search=  test  ")
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_status_filter_returns_only_matching(client):
    client.post("/tasks", json={"title": "Task 1", "status": "ToDo"})
    client.post("/tasks", json={"title": "Task 2", "status": "InProgress"})
    
    response = client.get("/tasks?status=ToDo")
    assert response.status_code == 200
    tasks = response.json()
    assert len(tasks) == 1
    assert tasks[0]["status"] == "ToDo"


def test_priority_filter_returns_only_matching(client):
    client.post("/tasks", json={"title": "Task 1", "priority": "High"})
    client.post("/tasks", json={"title": "Task 2", "priority": "Low"})
    
    response = client.get("/tasks?priority=High")
    assert response.status_code == 200
    tasks = response.json()
    assert len(tasks) == 1
    assert tasks[0]["priority"] == "High"


def test_combined_status_and_priority_filter(client):
    client.post("/tasks", json={"title": "Task 1", "status": "ToDo", "priority": "High"})
    client.post("/tasks", json={"title": "Task 2", "status": "ToDo", "priority": "Low"})
    client.post("/tasks", json={"title": "Task 3", "status": "InProgress", "priority": "High"})
    
    response = client.get("/tasks?status=ToDo&priority=High")
    assert response.status_code == 200
    tasks = response.json()
    assert len(tasks) == 1
    assert tasks[0]["status"] == "ToDo"
    assert tasks[0]["priority"] == "High"


def test_combined_search_and_status(client):
    client.post("/tasks", json={"title": "Fix bug", "status": "ToDo"})
    client.post("/tasks", json={"title": "Fix bug", "status": "InProgress"})
    
    response = client.get("/tasks?search=bug&status=ToDo")
    assert response.status_code == 200
    tasks = response.json()
    assert len(tasks) == 1
    assert tasks[0]["status"] == "ToDo"


def test_combined_search_and_priority(client):
    client.post("/tasks", json={"title": "Important task", "priority": "High"})
    client.post("/tasks", json={"title": "Important task", "priority": "Low"})
    
    response = client.get("/tasks?search=important&priority=High")
    assert response.status_code == 200
    tasks = response.json()
    assert len(tasks) == 1
    assert tasks[0]["priority"] == "High"


def test_combined_search_status_and_priority(client):
    client.post("/tasks", json={"title": "Critical bug", "status": "ToDo", "priority": "High"})
    client.post("/tasks", json={"title": "Critical bug", "status": "InProgress", "priority": "High"})
    client.post("/tasks", json={"title": "Critical bug", "status": "ToDo", "priority": "Low"})
    
    response = client.get("/tasks?search=critical&status=ToDo&priority=High")
    assert response.status_code == 200
    tasks = response.json()
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Critical bug"


def test_no_results_returns_200_with_empty_list(client):
    response = client.get("/tasks?search=nonexistent")
    assert response.status_code == 200
    assert response.json() == []


def test_invalid_status_returns_422(client):
    response = client.get("/tasks?status=InvalidStatus")
    assert response.status_code == 422


def test_invalid_priority_returns_422(client):
    response = client.get("/tasks?priority=InvalidPriority")
    assert response.status_code == 422


def test_create_task_with_valid_due_date(client):
    response = client.post("/tasks", json={"title": "Task with due date", "due_date": "2025-12-31"})
    assert response.status_code == 201
    data = response.json()
    assert data["due_date"] == "2025-12-31"


def test_create_task_with_invalid_date_format_returns_422(client):
    response = client.post("/tasks", json={"title": "Task", "due_date": "invalid-date"})
    assert response.status_code == 422


def test_update_task_due_date(client, created_task):
    response = client.patch(f"/tasks/{created_task['id']}", json={"due_date": "2025-06-15"})
    assert response.status_code == 200
    data = response.json()
    assert data["due_date"] == "2025-06-15"


def test_remove_task_due_date(client, created_task):
    client.patch(f"/tasks/{created_task['id']}", json={"due_date": "2025-06-15"})
    response = client.patch(f"/tasks/{created_task['id']}", json={"due_date": None})
    assert response.status_code == 200
    data = response.json()
    assert data["due_date"] is None


def test_overdue_filter_returns_only_overdue_tasks(client):
    yesterday = date.today() - timedelta(days=1)
    tomorrow = date.today() + timedelta(days=1)
    
    client.post("/tasks", json={"title": "Overdue task", "due_date": yesterday.isoformat(), "status": "ToDo"})
    client.post("/tasks", json={"title": "Future task", "due_date": tomorrow.isoformat(), "status": "ToDo"})
    client.post("/tasks", json={"title": "No due date task", "status": "ToDo"})
    
    response = client.get("/tasks?overdue=true")
    assert response.status_code == 200
    tasks = response.json()
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Overdue task"


def test_completed_task_not_considered_overdue(client):
    yesterday = date.today() - timedelta(days=1)
    
    client.post("/tasks", json={"title": "Done task", "due_date": yesterday.isoformat(), "status": "Done"})
    
    response = client.get("/tasks?overdue=true")
    assert response.status_code == 200
    tasks = response.json()
    assert len(tasks) == 0


def test_task_without_due_date_not_considered_overdue(client):
    client.post("/tasks", json={"title": "No due date", "status": "ToDo"})
    
    response = client.get("/tasks?overdue=true")
    assert response.status_code == 200
    tasks = response.json()
    assert len(tasks) == 0


def test_overdue_false_returns_all_tasks(client):
    yesterday = date.today() - timedelta(days=1)
    
    client.post("/tasks", json={"title": "Overdue task", "due_date": yesterday.isoformat(), "status": "ToDo"})
    client.post("/tasks", json={"title": "Normal task", "status": "ToDo"})
    
    response = client.get("/tasks?overdue=false")
    assert response.status_code == 200
    tasks = response.json()
    assert len(tasks) == 2


def test_get_version_returns_version_string(client):
    response = client.get("/version")
    assert response.status_code == 200
    data = response.json()
    assert "version" in data
    assert data["version"] == "0.1.0"
