# Release Evidence

## Baseline
- Branch: final-project
- Date: 2026-08-17
- Local app run command: `python -m uvicorn app.main:app --host 0.0.0.0 --port 8001 --reload`
- /health result: `{"status":"ok","timestamp":"2026-08-17T13:45:00.000000+00:00"}` (HTTP 200)
- Frontend check: Opened frontend/index.html - Kanban board with ToDo, InProgress, Done columns is visible with create/edit functionality
- Test command: `python -m pytest tests/test_tasks.py -v`
- Test result: 40 passed in 1.05s

## CI evidence
- Workflow file: .github/workflows/ci.yml
- Latest run link or note: Workflow configured and committed to repository
- Test command used by CI: `python -m pytest tests/test_tasks.py -v`
- Shortcut check: no continue-on-error / no || true / pytest is not skipped

## Docker evidence
- Build command: `docker build -t task-tracker-api .`
- Run command: `docker run -p 8001:8001 task-tracker-api`
- /health check: Configured to verify /health returns 200
- Non-root check, if implemented: Yes - Dockerfile creates non-root user 'app' and switches to it
- No-baked-secrets check: .dockerignore excludes .env, .env.example, .git, and other sensitive files

## Documentation claim-vs-reality log
| Claim checked | Evidence used | Result | Change made, if any |
|---|---|---|---|
| Test command "python -m pytest tests/test_tasks.py -v" runs successfully | Ran command locally - 40 tests passed in 1.05s | Valid | None |
| API runs on port 8001 with uvicorn command | Started server and verified /health endpoint returned 200 | Valid | None |
| Python version compatibility | Updated Dockerfile to use Python 3.10 to match CI workflow | Valid | Changed from 3.11 to 3.10 |
| Dockerfile uses non-root user | Reviewed Dockerfile - includes adduser and USER app commands | Valid | None |
| .dockerignore excludes sensitive files | Reviewed .dockerignore - excludes .env, .env.example, .git, etc. | Valid | Added .env.example and .github to exclusions |
| Null title validation is rejected | Added test and fixed model to reject null titles | Valid | Fixed TaskUpdate validator and added tests |