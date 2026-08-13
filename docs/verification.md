# Verification Report

## Baseline Verification

### Existing Application Behavior (Before Implementation)
- Tasks could be created with title, description, status, priority, assignee
- GET /tasks supported optional status and priority filtering
- Frontend displayed all tasks in Kanban board (ToDo, InProgress, Done)
- No search functionality
- No combined filters
- No due date field
- No overdue indicator
- Drag and drop between columns worked
- Status transition validation enforced (ToDo→Done rejected)

### Existing Tests Before Implementation
- 16 tests in test_tasks.py
- Tests covered: CRUD operations, validation, status transitions, basic filtering
- All tests passing

---

## Backend Tests

### Tests Executed
Ran: `python3 -m pytest tests/test_tasks.py -v`

### Results
**Total: 38 tests passed, 1 warning**

#### Existing Tests (16) - All Passing
- test_create_task_valid_returns_201_with_full_body
- test_create_task_missing_title_returns_422
- test_create_task_blank_title_returns_422
- test_create_task_invalid_priority_returns_422
- test_create_task_unknown_field_returns_422
- test_list_tasks_empty_returns_200_and_empty_list
- test_list_tasks_filter_by_status_no_match_returns_200_and_empty_list
- test_list_tasks_filter_by_priority_returns_only_matches
- test_get_task_by_id_returns_task
- test_get_task_by_id_not_found_returns_404_with_detail
- test_patch_partial_update_keeps_other_fields
- test_patch_not_found_returns_404
- test_patch_valid_transition_todo_to_inprogress_returns_200
- test_patch_invalid_transition_todo_to_done_returns_422
- test_patch_same_status_returns_422
- test_delete_existing_returns_204_no_body
- test_delete_missing_returns_404

#### Feature 1 New Tests (14) - All Passing
- test_search_title_returns_matching_tasks
- test_search_description_returns_matching_tasks
- test_search_case_insensitive
- test_search_trims_whitespace
- test_status_filter_returns_only_matching
- test_priority_filter_returns_only_matching
- test_combined_status_and_priority_filter
- test_combined_search_and_status
- test_combined_search_and_priority
- test_combined_search_status_and_priority
- test_no_results_returns_200_with_empty_list
- test_invalid_status_returns_422
- test_invalid_priority_returns_422

#### Feature 2 New Tests (8) - All Passing
- test_create_task_with_valid_due_date
- test_create_task_with_invalid_date_format_returns_422
- test_update_task_due_date
- test_remove_task_due_date
- test_overdue_filter_returns_only_overdue_tasks
- test_completed_task_not_considered_overdue
- test_task_without_due_date_not_considered_overdue
- test_overdue_false_returns_all_tasks

### New Tests Added
- 22 new tests total (14 for Feature 1, 8 for Feature 2)
- Tests cover: search functionality, combined filters, validation, due date CRUD, overdue detection, edge cases

---

## Manual Browser Verification

### Checklist Results

#### Search + Combined Filters
- [x] Type in search box - tasks filter in real-time
- [x] Search matches title text
- [x] Search matches description text
- [x] Status dropdown filters correctly
- [x] Priority dropdown filters correctly
- [x] Combined filters work together (e.g., search + status)
- [x] Clear Filters button resets all filters
- [x] Empty state shows when no tasks match

#### Due Dates
- [x] Create task with due date
- [x] Edit task to add/change due date
- [x] Edit task to remove due date (clear the date field)
- [x] Due date displays on task card
- [x] Overdue badge appears for past-due tasks (not Done)
- [x] Overdue checkbox filters only overdue tasks
- [x] Completed tasks don't show overdue badge

#### Existing Functionality
- [x] Create task still works
- [x] Edit task still works
- [x] Delete task still works
- [x] Drag and drop between columns still works
- [x] Status transition validation still works (ToDo→Done rejected)

---

## Behavior Contract

### Before Implementation

**GET /tasks**
- Query params: `status` (optional), `priority` (optional)
- Returns: list of tasks filtered by status and/or priority
- Invalid status/priority: HTTP 422

**Task Model**
- Fields: id, title, description, status, priority, assignee, created_at, updated_at
- No due_date field

**Frontend**
- No search/filter UI
- No due date display
- No overdue indicator

### After Implementation

**GET /tasks**
- Query params: `status` (optional), `priority` (optional), `search` (optional), `assignee` (optional), `overdue` (optional)
- Returns: list of tasks filtered by any combination of parameters
- Search: case-insensitive match on title OR description, trims whitespace
- Assignee: case-insensitive substring match
- Overdue: tasks with due_date < today AND status != Done
- Invalid status/priority: HTTP 422 (preserved)

**Task Model**
- Fields: id, title, description, status, priority, assignee, due_date (optional), created_at, updated_at

**Frontend**
- Filter bar with search input, status dropdown, priority dropdown, overdue checkbox, clear button
- Due date displayed on task cards
- Overdue badge on past-due tasks (not Done)
- Real-time filtering on input/change events

### Observable Behavior Changes
- **Added:** Search functionality (title + description)
- **Added:** Assignee filtering
- **Added:** Due date field on tasks
- **Added:** Overdue badge on task cards
- **Added:** Overdue filter
- **Added:** Filter bar UI
- **Preserved:** All existing CRUD operations
- **Preserved:** Status transition validation
- **Preserved:** Drag and drop functionality
- **Preserved:** Existing status/priority filtering behavior

---

## Break Tests

### Break Test 1: Search Functionality

**Protected Behavior:** Search should return tasks matching title or description case-insensitively.

**Temporary Code Change:**
```python
# In storage.py, get_all_tasks()
# Changed from:
if search:
    search_term = search.strip().lower()
    tasks = [t for t in tasks if search_term in t.title.lower() or search_term in t.description.lower()]

# Changed to:
if search:
    search_term = search.strip()  # Removed .lower()
    tasks = [t for t in tasks if search_term in t.title or search_term in t.description]  # Removed .lower()
```

**Expected Failure:** `test_search_case_insensitive` should fail because search is now case-sensitive.

**Actual Failure:**
```
FAILED tests/test_tasks.py::test_search_case_insensitive - AssertionError: assert len(response.json()) == 1
```

**Restoration:** Reverted the change to restore case-insensitive matching.

**Successful Rerun:** All 38 tests passed.

---

### Break Test 2: Overdue Logic

**Protected Behavior:** Completed tasks (status = Done) should not be considered overdue even if past due date.

**Temporary Code Change:**
```python
# In storage.py, get_all_tasks()
# Changed from:
if overdue:
    today = date.today()
    tasks = [t for t in tasks if t.due_date and t.due_date < today and t.status.value != "Done"]

# Changed to:
if overdue:
    today = date.today()
    tasks = [t for t in tasks if t.due_date and t.due_date < today]  # Removed status check
```

**Expected Failure:** `test_completed_task_not_considered_overdue` should fail because completed tasks are now included in overdue results.

**Actual Failure:**
```
FAILED tests/test_tasks.py::test_completed_task_not_considered_overdue - AssertionError: assert len(tasks) == 0
```

**Restoration:** Reverted the change to restore the status check.

**Successful Rerun:** All 38 tests passed.
