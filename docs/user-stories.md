# User Stories

## Feature 1: Search + Combined Filters

### US-1: Search Tasks by Title or Description
**As a** user  
**I want** to search for tasks by typing text  
**So that** I can quickly find specific tasks without scrolling

**Acceptance Criteria:**
- Search input field is visible above the Kanban board
- Search matches text in task titles (case-insensitive)
- Search matches text in task descriptions (case-insensitive)
- Search trims whitespace before matching
- Search filters in real-time as user types
- No matching tasks returns empty state with "No tasks" message
- Kanban columns remain visible even when no tasks match

### US-2: Filter Tasks by Status
**As a** user  
**I want** to filter tasks by status  
**So that** I can focus on tasks in a specific state

**Acceptance Criteria:**
- Status dropdown is visible in filter bar
- Dropdown includes "All", "To Do", "In Progress", "Done"
- Selecting a status filters tasks immediately
- Invalid status values return HTTP 422 (backend validation preserved)
- Filter can be combined with other filters

### US-3: Filter Tasks by Priority
**As a** user  
**I want** to filter tasks by priority  
**So that** I can focus on high-priority items

**Acceptance Criteria:**
- Priority dropdown is visible in filter bar
- Dropdown includes "All", "Low", "Medium", "High"
- Selecting a priority filters tasks immediately
- Invalid priority values return HTTP 422 (backend validation preserved)
- Filter can be combined with other filters

### US-4: Combine Multiple Filters
**As a** user  
**I want** to apply multiple filters at once  
**So that** I can narrow down to specific tasks

**Acceptance Criteria:**
- Search + status filter works together
- Search + priority filter works together
- Status + priority filter works together
- Search + status + priority filter works together
- All filters can be cleared with one button

### US-5: Clear All Filters
**As a** user  
**I want** to reset all filters to default  
**So that** I can quickly return to viewing all tasks

**Acceptance Criteria:**
- "Clear Filters" button is visible
- Clicking clears search input
- Clicking resets status dropdown to "All"
- Clicking resets priority dropdown to "All"
- All tasks are displayed after clearing

### AI Assumption Corrected
**Placeholder – No AI assumptions were explicitly corrected during this implementation.** The AI made reasonable defaults for date format (YYYY-MM-DD), overdue logic (completed tasks not overdue), and assignee filtering (case-insensitive), and these were accepted without modification.

---

## Feature 2: Due Dates + Overdue Filter

### US-6: Set Due Date on Task
**As a** user  
**I want** to set a due date when creating or editing a task  
**So that** I can track when tasks need to be completed

**Acceptance Criteria:**
- Due date field is visible in task modal
- Due date is optional (can be left blank)
- Due date uses date picker (YYYY-MM-DD format)
- Invalid date formats return HTTP 422
- Due date is saved and displayed on task card

### US-7: Edit or Remove Due Date
**As a** user  
**I want** to change or remove a due date  
**So that** I can adjust task deadlines as needed

**Acceptance Criteria:**
- Due date field populates with existing value when editing
- Due date can be changed to a new valid date
- Due date can be removed by clearing the field
- Changes are saved immediately

### US-8: View Due Date on Task Card
**As a** user  
**I want** to see the due date on task cards  
**So that** I can quickly identify upcoming deadlines

**Acceptance Criteria:**
- Due date is displayed on each task card (if set)
- Due date format is readable (YYYY-MM-DD)
- Due date appears below priority and assignee

### US-9: See Overdue Indicator
**As a** user  
**I want** to see which tasks are overdue  
**So that** I can prioritize late tasks

**Acceptance Criteria:**
- Overdue badge appears on task cards when due date has passed
- Overdue badge is red/pink colored for visibility
- Completed tasks (status = Done) do not show overdue badge
- Tasks without due dates do not show overdue badge

### US-10: Filter Overdue Tasks
**As a** user  
**I want** to filter to show only overdue tasks  
**So that** I can focus on late items

**Acceptance Criteria:**
- Overdue checkbox is visible in filter bar
- Checking checkbox shows only overdue tasks
- Unchecking checkbox shows all tasks
- Overdue filter can be combined with other filters
- Completed tasks are excluded from overdue results

### AI Assumption Corrected
**Placeholder – No AI assumptions were explicitly corrected during this implementation.** The AI computed overdue status in the backend rather than frontend, which was accepted as consistent with the existing architecture.
