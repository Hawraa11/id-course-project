@echo off
REM Task Tracker API - Curl Test Script (Windows)
REM Tests all endpoints: health, create, list, get, update, delete

set BASE_URL=http://localhost:8000

echo ==========================================
echo Task Tracker API - Curl Tests
echo ==========================================
echo.

REM Test 1: Health Check
echo Test 1: GET /health
curl -s -X GET "%BASE_URL%/health"
echo.
echo.

REM Test 2: Create a task
echo Test 2: POST /tasks - Create task
curl -s -X POST "%BASE_URL%/tasks" -H "Content-Type: application/json" -d "{\"title\": \"Test Task\", \"description\": \"This is a test task\", \"priority\": \"High\"}"
echo.
echo.

REM Test 3: Create another task for filtering tests
echo Test 3: POST /tasks - Create second task
curl -s -X POST "%BASE_URL%/tasks" -H "Content-Type: application/json" -d "{\"title\": \"Low Priority Task\", \"priority\": \"Low\"}"
echo.
echo.

REM Test 4: List all tasks
echo Test 4: GET /tasks - List all tasks
curl -s -X GET "%BASE_URL%/tasks"
echo.
echo.

REM Test 5: List tasks filtered by priority
echo Test 5: GET /tasks?priority=High - Filter by priority
curl -s -X GET "%BASE_URL%/tasks?priority=High"
echo.
echo.

REM Test 6: List tasks filtered by status
echo Test 6: GET /tasks?status=ToDo - Filter by status
curl -s -X GET "%BASE_URL%/tasks?status=ToDo"
echo.
echo.

REM Test 7: Get specific task by ID (using a placeholder ID)
echo Test 7: GET /tasks/{id} - Get task by ID (replace {id} with actual task ID)
curl -s -X GET "%BASE_URL%/tasks/1"
echo.
echo.

REM Test 8: Update task title (partial update)
echo Test 8: PATCH /tasks/{id} - Update title (replace {id} with actual task ID)
curl -s -X PATCH "%BASE_URL%/tasks/1" -H "Content-Type: application/json" -d "{\"title\": \"Updated Test Task\"}"
echo.
echo.

REM Test 9: Update task status (valid transition: ToDo -> InProgress)
echo Test 9: PATCH /tasks/{id} - Update status to InProgress (replace {id} with actual task ID)
curl -s -X PATCH "%BASE_URL%/tasks/1" -H "Content-Type: application/json" -d "{\"status\": \"InProgress\"}"
echo.
echo.

REM Test 10: Update task status (valid transition: InProgress -> Done)
echo Test 10: PATCH /tasks/{id} - Update status to Done (replace {id} with actual task ID)
curl -s -X PATCH "%BASE_URL%/tasks/1" -H "Content-Type: application/json" -d "{\"status\": \"Done\"}"
echo.
echo.

REM Test 11: Try invalid status transition (should fail)
echo Test 11: PATCH /tasks/{id} - Invalid transition (should fail with 422)
curl -s -X PATCH "%BASE_URL%/tasks/1" -H "Content-Type: application/json" -d "{\"status\": \"ToDo\"}"
echo.
echo.

REM Test 12: Get non-existent task (should fail with 404)
echo Test 12: GET /tasks/999 - Non-existent task (should fail with 404)
curl -s -X GET "%BASE_URL%/tasks/999"
echo.
echo.

REM Test 13: Delete task
echo Test 13: DELETE /tasks/{id} - Delete task (replace {id} with actual task ID)
curl -s -X DELETE "%BASE_URL%/tasks/1"
echo.
echo.

REM Test 14: Validation - Create task with missing title (empty JSON)
echo Test 14: POST /tasks - Missing title validation (should fail with 422)
curl -s -X POST "%BASE_URL%/tasks" -H "Content-Type: application/json" -d "{}"
echo.
echo.

REM Test 15: Validation - Create task with blank title (spaces)
echo Test 15: POST /tasks - Blank title validation (should fail with 422)
curl -s -X POST "%BASE_URL%/tasks" -H "Content-Type: application/json" -d "{\"title\": \"   \"}"
echo.
echo.

REM Test 16: Validation - Create task with invalid priority (should fail)
echo Test 16: POST /tasks - Invalid priority (should fail with 422)
curl -s -X POST "%BASE_URL%/tasks" -H "Content-Type: application/json" -d "{\"title\": \"Test\", \"priority\": \"Invalid\"}"
echo.
echo.

REM Test 17: Validation - Create task with unknown field (should fail)
echo Test 17: POST /tasks - Unknown field (should fail with 422)
curl -s -X POST "%BASE_URL%/tasks" -H "Content-Type: application/json" -d "{\"title\": \"Test\", \"unknown\": \"field\"}"
echo.
echo.

REM Test 18: Invalid status transition - same status (should fail with 422)
echo Test 18: PATCH /tasks/{id} - Same status transition (should fail with 422)
curl -s -X PATCH "%BASE_URL%/tasks/1" -H "Content-Type: application/json" -d "{\"status\": \"ToDo\"}"
echo.
echo.

echo ==========================================
echo All tests completed!
echo ==========================================
