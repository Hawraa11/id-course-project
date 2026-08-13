# Claude Context for Task Tracker API

## Project Overview
This is a FastAPI-based task management application with a Kanban board interface. It demonstrates REST API design, Pydantic validation, in-memory storage, and frontend integration. The project is a learning skeleton for Module 1.

## Tech Stack
- **Backend**: FastAPI 0.115.0
- **Server**: Uvicorn 0.30.6 (with standard extras)
- **Validation**: Pydantic 2.9.2
- **Environment**: python-dotenv 1.0.1
- **Testing**: pytest
- **Frontend**: Vanilla HTML/JS (single-page application)

## Architecture

### Backend Structure
```
app/
├── __init__.py          # Package initialization
├── main.py              # FastAPI application and endpoints
├── models.py            # Pydantic models (TaskCreate, TaskUpdate, TaskResponse)
├── storage.py           # In-memory task storage with CRUD operations
└── business_rules.py    # Status transition validation logic
```

### Key Components

**app/main.py**
- FastAPI application setup with CORS middleware
- Endpoints: `/health`, `/tasks` (CRUD operations)
- Environment-based configuration (PORT, APP_ENV)
- Auto-generated docs at `/docs` (Swagger UI)

**app/models.py**
- `TaskStatus` enum: ToDo, InProgress, Done
- `TaskPriority` enum: Low, Medium, High
- `TaskCreate`: Request model for creating tasks
- `TaskUpdate`: Request model for updating tasks (all fields optional)
- `TaskResponse`: Response model with all task fields including timestamps
- Field validators: title cannot be blank, max 200 characters

**app/storage.py**
- In-memory dictionary-based storage (`_tasks: dict[str, TaskResponse]`)
- Functions: `add_task`, `get_all_tasks`, `get_task_by_id`, `update_task`, `delete_task`, `_reset`
- Filtering support: status, priority, search (title/description), assignee, overdue
- Overdue logic: due_date < today AND status != Done

**app/business_rules.py**
- Valid status transitions:
  - ToDo → InProgress ✓
  - InProgress → Done ✓
  - Done → InProgress ✓
  - ToDo → Done ✗ (must go through InProgress)
  - Same status ✗ (no-op not allowed)
- Raises HTTP 422 for invalid transitions

### Frontend
- Single HTML file: `frontend/index.html`
- Kanban board with ToDo, InProgress, Done columns
- Drag & drop functionality
- Real-time search and filtering
- Connects to API at `http://localhost:8001`

## Running the Application

### Setup
```bash
python -m venv venv
venv\Scripts\activate          # Windows
pip install -r requirements.txt
pip install pytest
copy .env.example .env         # Windows
```

### Start Server
```bash
python -m uvicorn app.main:app --host 0.0.0.0 --port 8001 --reload
```

Or run directly:
```bash
python -m app.main
```

### Access
- API: http://localhost:8001
- Docs: http://localhost:8001/docs
- Frontend: Open `frontend/index.html` in browser

## API Endpoints

### Tasks
- `POST /tasks` - Create task (returns 201)
- `GET /tasks` - List tasks with optional filters
- `GET /tasks/{task_id}` - Get specific task (404 if not found)
- `PATCH /tasks/{task_id}` - Update task (404 if not found, 422 for invalid status transition)
- `DELETE /tasks/{task_id}` - Delete task (204 on success, 404 if not found)

### Query Parameters (GET /tasks)
- `search` - Case-insensitive search in title and description
- `status` - Filter by TaskStatus
- `priority` - Filter by TaskPriority
- `assignee` - Case-insensitive filter by assignee
- `overdue` - Boolean filter for overdue tasks

### Health
- `GET /health` - Returns `{"status": "ok", "timestamp": "ISO8601"}`

## Testing

### Test Structure
```
tests/
├── conftest.py       # Pytest fixtures (client, created_task, storage reset)
└── test_tasks.py     # 38 tests covering CRUD, validation, filtering
```

### Run Tests
```bash
python -m pytest tests/test_tasks.py -v
```

### Fixtures
- `_reset_storage` (autouse): Clears in-memory storage before/after each test
- `client`: FastAPI TestClient instance
- `created_task`: Creates a sample task for tests

## Business Rules Summary

1. **Title Validation**
   - Cannot be blank after trimming whitespace
   - Maximum 200 characters

2. **Status Transitions**
   - Must follow valid transition paths
   - Cannot skip InProgress when going from ToDo to Done
   - Cannot update to same status

3. **Overdue Detection**
   - Task has a due_date
   - Today's date > due_date
   - Task status is not Done

4. **Extra Fields**
   - Request models use `extra="forbid"` to reject unknown fields

## Environment Variables
- `PORT`: Server port (default: 8000)
- `APP_ENV`: Environment mode (default: development)

## Important Notes
- Data is stored in-memory and lost on server restart
- CORS is enabled for all origins (development setup)
- IDs are sequential integers as strings
- Timestamps are in UTC timezone
- The project includes comprehensive documentation in `docs/` folder (user-stories.md, mini-adr.md, prompt-log.md, verification.md, reflection.md)
