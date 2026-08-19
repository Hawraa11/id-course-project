# Architecture Decision Record: Search + Combined Filters and Due Dates + Overdue Filter

## Context
The existing Task Tracker application used in-memory storage with basic CRUD operations. The GET /tasks endpoint supported optional status and priority filtering. The frontend displayed all tasks in a Kanban board with no search or filtering UI. Tasks had no due date field.

The requirement was to add two features:
1. Search + Combined Filters (search, status, priority, assignee)
2. Due Dates + Overdue Filter

## Decision

### Feature 1: Search + Combined Filters
- Extended GET /tasks endpoint with optional `search` and `assignee` query parameters
- Implemented filtering logic in `storage.get_all_tasks()` using list comprehensions
- Search: case-insensitive substring match on title OR description, with whitespace trimming
- Assignee: case-insensitive substring match on assignee field
- Frontend: Added filter bar with search input, status dropdown, priority dropdown, and clear button
- Filters apply in real-time via event listeners (input/change events)

### Feature 2: Due Dates + Overdue Filter
- Added `due_date: Optional[date]` field to TaskCreate, TaskUpdate, and TaskResponse models
- Extended GET /tasks endpoint with optional `overdue: bool` query parameter
- Overdue computed in backend: task has due_date AND today > due_date AND status != Done
- Frontend: Added date input field to modal, displays due date on cards, shows overdue badge
- Frontend: Added overdue checkbox to filter bar

## Rationale

### Backend Computation of Overdue
**Decision:** Compute overdue status in the backend storage layer.

**Reasoning:**
- Consistent with existing architecture (all filtering logic already in storage.py)
- Frontend already relies on backend for all task data
- Avoids timezone inconsistencies between client and server
- Simpler to test (backend tests cover the logic)
- Reuses existing filtering pattern in `get_all_tasks()`

### Date Format
**Decision:** Use `date` type (YYYY-MM-DD) not `datetime`.

**Reasoning:**
- Simpler for users (no time component to worry about)
- Matches HTML5 `<input type="date">` behavior
- Pydantic validates automatically
- Sufficient for task deadlines (time of day not critical)

### Completed Tasks Not Overdue
**Decision:** Tasks with status "Done" are not considered overdue regardless of due date.

**Reasoning:**
- Common business rule (completed tasks are not "late")
- Focuses overdue filter on actionable items
- Matches user expectation (done tasks shouldn't flag as problems)

## Alternatives Suggested by AI

### Frontend Overdue Computation
**Alternative:** Compute overdue status in JavaScript on the client side.

**Rejected:** Too complex. Would require:
- Date parsing and comparison in JavaScript
- Potential timezone issues
- Duplicate logic if API is used by other clients
- Harder to test consistently

### SQLAlchemy/Database Migration
**Alternative:** Migrate from in-memory storage to SQLite with SQLAlchemy.

**Rejected:** Out of scope. The project constraints explicitly stated:
- Do not introduce new frameworks
- Do not replace the architecture
- Reuse current project structure wherever possible

The existing in-memory dict storage was sufficient and consistent with the learning project scope.

### Full-Text Search Library
**Alternative:** Use a dedicated search library like Whoosh or Elasticsearch.

**Rejected:** Over-engineering. Simple substring matching is sufficient for:
- Small dataset (in-memory)
- Learning project scope
- No complex search requirements (fuzzy matching, ranking, etc.)

## Trade-offs

### Backend Overdue Computation
**Pros:**
- Consistent with existing architecture
- Single source of truth
- Easier to test
- No client-side timezone issues

**Cons:**
- Backend must be aware of "current date" (uses `date.today()`)
- Slight coupling between storage and business logic (acceptable for this scope)

### In-Memory Storage
**Pros:**
- Simple, no database setup
- Fast for learning project
- Easy to reset between tests

**Cons:**
- Data lost on server restart
- Not production-ready (acceptable for learning project)

## Risks if Feature Grows

### Search Complexity
If search requirements grow (fuzzy matching, ranking, synonyms), the current substring approach will not scale. Would need to consider:
- Full-text search library
- Database with search capabilities
- Dedicated search service

### Overdue Logic
If overdue rules become more complex (business hours, holidays, grace periods), the simple date comparison will need to be extracted into a dedicated service layer.

### Frontend Performance
If task count grows significantly, real-time filtering on every keystroke may cause performance issues. Would need:
- Debouncing on search input
- Pagination
- Virtual scrolling

## Scope Limitations

- No authentication or user-specific filtering
- No sorting by due date
- No recurring due dates
- No due date reminders/notifications
- No bulk operations on filtered tasks
- No saved filter presets
- In-memory storage (data persistence not required)
