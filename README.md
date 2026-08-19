# Task Tracker API

A FastAPI-based task management application with a Kanban board interface. This project demonstrates REST API design, Pydantic validation, in-memory storage, and frontend integration.

## Features

- **Task CRUD:** Create, read, update, and delete tasks
- **Kanban Board:** Visual task management with ToDo, In Progress, and Done columns
- **Search & Filters:** Search by title/description, filter by status, priority, assignee
- **Due Dates:** Optional due dates with overdue detection
- **Drag & Drop:** Move tasks between columns
- **Status Validation:** Enforced status transitions (ToDo→InProgress→Done)
- **Real-time Filtering:** Instant search and filter updates

## Project structure

```
task-tracker-api/
├── app/
│   ├── __init__.py
│   ├── main.py           # FastAPI endpoints
│   ├── models.py         # Pydantic models
│   ├── storage.py        # In-memory task storage
│   └── business_rules.py # Status transition validation
├── frontend/
│   └── index.html        # Single-page Kanban board
├── tests/
│   ├── conftest.py       # Pytest fixtures
│   └── test_tasks.py     # API tests
├── docs/                 # Project documentation
│   ├── midcourse/        # Mid-course project documents
│   │   ├── user-stories.md
│   │   ├── mini-adr.md
│   │   ├── prompt-log.md
│   │   ├── verification.md
│   │   └── reflection.md
│   ├── release-evidence.md
│   ├── final-ai-review.md
│   └── ai-playbook.md
├── .github/
│   └── workflows/
│       └── ci.yml
├── AGENTS.md
├── .env.example
├── .gitignore
├── Dockerfile
├── .dockerignore
├── requirements.txt
├── pytest.ini
└── README.md
```

## Setup

1. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate      # macOS/Linux
   venv\Scripts\activate         # Windows
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   pip install pytest
   ```

3. Copy the environment file and adjust if needed:

   ```bash
   cp .env.example .env       # macOS/Linux/Git Bash
   copy .env.example .env     # Windows (cmd.exe)
   ```

## Running the app

Start the API server:

```bash
python -m uvicorn app.main:app --host 0.0.0.0 --port 8001 --reload
```

The API will be available at `http://localhost:8001`.

## Accessing the Frontend

Open `frontend/index.html` in your browser (double-click the file or open via File menu).

The frontend connects to the API at `http://localhost:8001` for task data.

## API Endpoints

### Tasks

- `POST /tasks` - Create a new task
- `GET /tasks` - List all tasks (supports filtering)
- `GET /tasks/{task_id}` - Get a specific task
- `PATCH /tasks/{task_id}` - Update a task
- `DELETE /tasks/{task_id}` - Delete a task

### Query Parameters (GET /tasks)

- `search` - Search in title and description (case-insensitive)
- `status` - Filter by status (ToDo, InProgress, Done)
- `priority` - Filter by priority (Low, Medium, High)
- `assignee` - Filter by assignee (case-insensitive)
- `overdue` - Filter overdue tasks (true/false)

### Health

- `GET /health` - Health check endpoint

## Testing

Run all tests:

```bash
python -m pytest tests/test_tasks.py -v
```

The test suite includes 41 tests covering:
- CRUD operations
- Validation
- Status transitions
- Search and filtering
- Due dates and overdue detection

## API Documentation

With the server running, open your browser to:

```
http://localhost:8001/docs
```

FastAPI auto-generates interactive Swagger UI docs at `/docs` (and a ReDoc alternative at `/redoc`).

## Task Model

- `id` - Unique identifier
- `title` - Task title (required, max 200 chars)
- `description` - Task description (optional)
- `status` - Task status (ToDo, InProgress, Done)
- `priority` - Task priority (Low, Medium, High)
- `assignee` - Assigned person (optional)
- `due_date` - Due date (optional, YYYY-MM-DD format)
- `created_at` - Creation timestamp
- `updated_at` - Last update timestamp

## Business Rules

- Title cannot be blank after trimming whitespace
- Status transitions are enforced:
  - ToDo → InProgress ✓
  - InProgress → Done ✓
  - Done → InProgress ✓
  - ToDo → Done ✗ (must go through InProgress)
  - Same status ✗ (no-op not allowed)
- A task is overdue when:
  - It has a due date
  - Today's date is later than the due date
  - The task is not completed (status != Done)

## Final Project

Branch reviewed: final-project

### What this submission demonstrates
- Existing Task Tracker app still runs inside the intended course scope
- CI runs the pytest suite on push and/or pull request
- Docker image builds and runs with /health returning 200
- AI review, security, and ownership evidence is in docs/

### How to run locally
```bash
# Setup
python -m venv venv
venv\Scripts\activate          # Windows
pip install -r requirements.txt
pip install pytest httpx
copy .env.example .env

# Run the API server
python -m uvicorn app.main:app --host 0.0.0.0 --port 8001 --reload
```

### How to run tests
```bash
python -m pytest tests/test_tasks.py -v
```

### How to run with Docker
```bash
# Build the Docker image
docker build -t task-tracker-api .

# Run the container
docker run -p 8001:8001 task-tracker-api

# Verify health endpoint
curl http://localhost:8001/health
# Or use PowerShell: Invoke-WebRequest -Uri http://localhost:8001/health -UseBasicParsing
```

### Evidence files
- docs/release-evidence.md
- docs/final-ai-review.md
- docs/ai-playbook.md

### AI assistance summary
AI helped draft or review: CI, Docker, docs, security, debugging
I verified the work by: tests, diff review, Docker, /health, manual scan
One AI suggestion I rejected or corrected: Updated Dockerfile to use Python 3.10 to match CI and local environment, added httpx and pytest to Docker build for testing capability
