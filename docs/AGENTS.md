# AGENTS.md - AI Agent Guidelines for Task Tracker

## Project Summary

The Task Tracker API is a FastAPI-based task management application with a Kanban board interface. It demonstrates REST API design, Pydantic v2 validation, in-memory storage, and frontend integration. This is a learning project for AI-assisted coding modules.

**Key characteristics:**
- In-memory task storage (data lost on server restart)
- No authentication or authorization
- CORS enabled for all origins (development setup)
- Single-page vanilla JavaScript frontend
- 39 tests covering CRUD, validation, status transitions, search, filtering, and due dates

## Tech Stack and Commands

**Dependencies (from requirements.txt):**
- fastapi==0.115.0
- uvicorn[standard]==0.30.6
- pydantic==2.9.2
- python-dotenv==1.0.1

**Run commands (from README.md and app/main.py):**
```bash
# Start the API server
python -m uvicorn app.main:app --host 0.0.0.0 --port 8001 --reload

# Alternative: run directly
python -m app.main
```

**Test commands (from README.md):**
```bash
# Run all tests
python -m pytest tests/test_tasks.py -v
```

**API access:**
- API: http://localhost:8001
- Interactive docs: http://localhost:8001/docs
- Frontend: Open frontend/index.html in browser

## Business Rules (Visible in Code)

### Task Status Values (from app/models.py)
- `ToDo` (TaskStatus.TODO)
- `InProgress` (TaskStatus.IN_PROGRESS)
- `Done` (TaskStatus.DONE)

### Task Priority Values (from app/models.py)
- `Low` (TaskPriority.LOW)
- `Medium` (TaskPriority.MEDIUM)
- `High` (TaskPriority.HIGH)

### Status Transition Rules (from app/business_rules.py)
Valid transitions in VALID_TRANSITIONS:
- ToDo → InProgress ✓
- InProgress → Done ✓
- Done → InProgress ✓

Invalid transitions (raise HTTP 422):
- ToDo → Done (must go through InProgress)
- Same status → Same status (no-op not allowed)
- Any transition not in VALID_TRANSITIONS

### Validation Rules (from app/models.py)
- **Title validation:**
  - Cannot be blank after trimming whitespace
  - Maximum 200 characters
  - Applies to both TaskCreate and TaskUpdate
- **Extra fields:** Request models use `extra="forbid"` to reject unknown fields

### Overdue Detection (from app/storage.py)
A task is overdue when:
- It has a due_date
- Today's date > due_date
- Task status != "Done"

### API Endpoints (from app/main.py)
- `GET /health` - Health check (returns status and timestamp)
- `GET /version` - API version (returns version string)
- `POST /tasks` - Create task (returns 201)
- `GET /tasks` - List tasks with optional filters (status, priority, search, assignee, overdue)
- `GET /tasks/{task_id}` - Get specific task (returns 404 if not found)
- `PATCH /tasks/{task_id}` - Update task (returns 404 if not found, 422 for invalid status transition)
- `DELETE /tasks/{task_id}` - Delete task (returns 204 on success, 404 if not found)

## Module 5 Guardrails

**Primary constraint:** This is a grading and governance module. Do not build new app features.

**Working mode:**
1. **Docs-first:** Prefer read-only analysis first. Edit files in docs/ only unless explicitly approved otherwise.
2. **Read-only by default:** Do not modify app/ during Module 5 unless explicitly asked for one specific minimal fix.
3. **One task per thread:** Focus on a single bounded task per conversation.
4. **Cite evidence:** When making claims about the repo, cite actual files you inspected (e.g., "from app/models.py line 8-11").
5. **No guessing:** If uncertain or a file is not visible, say so instead of guessing.

**Allowed actions:**
- Read and analyze any file in the repository
- Create or edit documentation in docs/
- Review and audit existing code
- Propose minimal fixes with explicit approval

**Restricted actions:**
- Adding new features to app/
- Modifying app/ without explicit user approval
- Running destructive commands
- Changing database schema (none exists, but principle applies)
- Adding authentication or deployment infrastructure

## Security and Governance Reminders

**Secrets management:**
- Do not paste or expose secrets, API keys, or credentials
- Do not read .env files (use .env.example as reference)
- Do not suggest hardcoding secrets

**Command safety:**
- Do not run destructive commands (rm, delete, drop, etc.)
- Do not run commands that modify system state without explicit approval
- Prefer read-only commands for analysis

**Evidence-based claims:**
- Cite specific files and line numbers when making assertions
- Verify claims against actual code before stating them
- Use grep or read tools to confirm behavior

**No invention:**
- Do not invent features, endpoints, or behaviors that don't exist
- Do not assume validation rules without reading the code
- Do not guess at API responses without testing or reading implementation

**Scope boundaries:**
- This is a learning project, not production-ready
- No database, no authentication, no deployment
- In-memory storage means data is ephemeral
- CORS is wide open for development (not production-appropriate)

## Repository Structure

```
task-tracker-api/
├── app/
│   ├── __init__.py
│   ├── main.py           # FastAPI endpoints and app configuration
│   ├── models.py         # Pydantic models and enums
│   ├── storage.py        # In-memory task storage
│   └── business_rules.py # Status transition validation
├── frontend/
│   └── index.html        # Single-page Kanban board
├── tests/
│   ├── conftest.py       # Pytest fixtures
│   └── test_tasks.py     # API tests (39 tests)
├── docs/
│   ├── AGENTS.md         # This file
│   ├── user-stories.md
│   ├── mini-adr.md
│   ├── prompt-log.md
│   ├── verification.md
│   └── reflection.md
├── .env.example
├── .gitignore
├── requirements.txt
├── pytest.ini
├── claude.md
└── README.md
```

## Testing Context

**Test fixtures (from tests/conftest.py):**
- `_reset_storage` (autouse): Clears in-memory storage before/after each test
- `client`: FastAPI TestClient instance
- `created_task`: Creates a sample task for tests

**Test coverage (from tests/test_tasks.py):**
- 39 tests covering:
  - CRUD operations (create, read, update, delete)
  - Validation (blank title, invalid priority, unknown fields)
  - Status transitions (valid and invalid)
  - Search and filtering (title, description, status, priority, assignee, overdue)
  - Due dates and overdue detection
