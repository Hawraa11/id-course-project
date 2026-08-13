# Prompt Log

## Feature 1: Search + Combined Filters

### Prompt 1: Initial Implementation Request
**Goal:** Implement Search + Combined Filters feature end-to-end

**Prompt Summary:** Detailed specification for implementing search and combined filters on the existing Task Tracker, including backend requirements (search, status, priority, assignee filters), frontend requirements (filter bar, empty states), and testing requirements.

**AI Response:** AI inspected the existing codebase, identified relevant files (models.py, main.py, storage.py, index.html, test_tasks.py), and created an implementation plan. AI asked for clarification on three assumptions: date format, completed task overdue handling, and assignee filter case sensitivity.

**What I Accepted:** The inspection and planning approach. The AI systematically reviewed the codebase before proposing changes.

**What I Edited:** None - the inspection was accurate.

**What I Rejected:** None.

**Why:** The AI followed the requested workflow (inspect before implement) and identified the correct files and patterns.

---

### Prompt 2: Clarification Response
**Goal:** Provide answers to AI's clarification questions

**Prompt Summary:** "continue" - instructing AI to proceed with reasonable defaults for the three unanswered questions.

**AI Response:** AI proceeded with defaults: YYYY-MM-DD date format, completed tasks not considered overdue, case-insensitive assignee filtering. AI then implemented the backend changes (main.py, storage.py) and frontend changes (index.html), followed by tests.

**What I Accepted:** The default choices for date format, overdue logic, and assignee filtering.

**What I Edited:** None.

**What I Rejected:** None.

**Why:** The defaults were reasonable and consistent with the existing architecture.

---

### Prompt 3: Test Execution
**Goal:** Run tests to verify Feature 1 implementation

**Prompt Summary:** AI ran pytest to verify the new search/filter tests passed.

**AI Response:** All 30 tests passed (16 existing + 14 new for Feature 1). AI then proceeded to implement Feature 2.

**What I Accepted:** The test results and decision to proceed to Feature 2.

**What I Edited:** None.

**What I Rejected:** None.

**Why:** Tests passing indicated Feature 1 was working correctly.

---

## Feature 2: Due Dates + Overdue Filter

### Prompt 4: Feature 2 Implementation
**Goal:** Implement Due Dates + Overdue Filter feature

**Prompt Summary:** AI continued with Feature 2 implementation based on the original specification, adding due_date field to models, overdue filter to API, and due date UI to frontend.

**AI Response:** AI added due_date field to TaskCreate, TaskUpdate, TaskResponse models, extended storage.get_all_tasks() with overdue logic, added overdue query parameter to API, added date input to modal, displayed due date on cards with overdue badge, and added overdue checkbox to filter bar.

**What I Accepted:** The backend computation of overdue status (in storage layer).

**What I Edited:** None.

**What I Rejected:** None.

**Why:** Backend computation was consistent with existing architecture and easier to test.

---

### Prompt 5: Feature 2 Tests
**Goal:** Add and run tests for Feature 2

**Prompt Summary:** AI added 8 new tests for due date CRUD and overdue filtering, then ran pytest.

**AI Response:** All 38 tests passed (30 from Feature 1 + 8 new for Feature 2). AI then started the server for manual verification.

**What I Accepted:** The test coverage and results.

**What I Edited:** None.

**What I Rejected:** None.

**Why:** Tests covered all required scenarios including edge cases.

---

### Prompt 6: Manual Verification Setup
**Goal:** Start server for manual browser testing

**Prompt Summary:** AI started the uvicorn server in background and provided browser preview.

**AI Response:** Server started on port 8001. AI provided manual verification checklist for both features.

**What I Accepted:** The verification checklist.

**What I Edited:** None.

**What I Rejected:** None.

**Why:** Checklist covered all important scenarios to verify manually.

---

## Weak Prompt

### Weak Prompt: "continue"
**Original:** User responded "continue" when AI asked for clarification on three assumptions (date format, completed task overdue handling, assignee filter case sensitivity).

**Why It Was Weak:**
- Did not specify which defaults to use
- Relied on AI to make architectural decisions
- Could have led to implementation that didn't match user expectations
- Missed opportunity to provide explicit requirements

**Stronger Prompt Rewrite:**
"Proceed with the following defaults: use YYYY-MM-DD date format (no time component), completed tasks should NOT be considered overdue even if past due date, and assignee filtering should be case-insensitive for better user experience."

**Why This Is Stronger:**
- Explicitly states the requirements
- Removes ambiguity
- Provides reasoning for the choices
- Ensures AI implements exactly what is wanted
