# Task Management CLI

A simple command-line interface (CLI) for managing tasks. This tool allows you to add, update, delete, and mark tasks as in-progress or done, as well as list tasks by status or all tasks. Tasks are stored persistently in a JSON file.

## Features
- Add new tasks with a description.
- Update task descriptions.
- Delete tasks.
- Mark tasks as `todo`, `in-progress`, or `done`.
- List all tasks or filter by status (`todo`, `in-progress`, `done`).
- Persistent storage using a JSON file.
- Timestamps for task creation and updates.

## Requirements
- Python 3.8 or higher
- Poetry (optional, for dependency management and CLI installation)

## Installation

### Step 1: Clone or Download the Project
Download the project files or clone the repository:
```bash
git clone <repository-url>
cd task-cli
```

### Step 2: Install Dependencies
The CLI depends on the `click` library. You can install it in one of two ways:

#### Option 1: Using Poetry (Recommended)
1. Install Poetry if you haven't already:
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```
   Or on Windows (PowerShell):
   ```bash
   (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
   ```

2. Install dependencies and set up the CLI:
   ```bash
   poetry install
   ```

3. Activate the virtual environment:
   ```bash
   poetry shell
   ```

#### Option 2: Using pip
1. Install `click`:
   ```bash
   pip install click
   ```

2. Run the CLI directly with Python:
   ```bash
   python task_cli.py --help
   ```

### Step 3: Verify Installation
Check if the CLI is installed correctly:
```bash
task-cli --help
```
Or, if using pip:
```bash
python task_cli.py --help
```

This should display the available commands and options.

## Usage
The CLI supports the following commands. Run `task-cli --help` or `task-cli <command> --help` for detailed help.

### Add a Task
```bash
task-cli add "Buy groceries"
```
Output: `Task added successfully (ID: 1)`

### Update a Task
```bash
task-cli update 1 "Buy groceries and cook dinner"
```
Output: `Task 1 updated successfully`

### Delete a Task
```bash
task-cli delete 1
```
Output: `Task 1 deleted successfully`

### Mark a Task as In-Progress
```bash
task-cli mark-in-progress 1
```
Output: `Task 1 marked as in-progress`

### Mark a Task as Done
```bash
task-cli mark-done 1
```
Output: `Task 1 marked as done`

### List All Tasks
```bash
task-cli list
```
Output: Lists all tasks with ID, status, description, creation, and update timestamps.

### List Tasks by Status
```bash
task-cli list todo
task-cli list in-progress
task-cli list done
```
Output: Lists tasks filtered by the specified status.

## Example Workflow
```bash
# Add tasks
task-cli add "Buy groceries"
task-cli add "Finish report"

# List all tasks
task-cli list

# Mark a task as in-progress
task-cli mark-in-progress 1

# Update a task
task-cli update 1 "Buy groceries and cook dinner"

# List in-progress tasks
task-cli list in-progress

# Mark a task as done
task-cli mark-done 1

# Delete a task
task-cli delete 2
```

## Task Storage
Tasks are stored in a `tasks.json` file in the project directory. Each task includes:
- `id`: Unique task identifier.
- `description`: Task description.
- `status`: `todo`, `in-progress`, or `done`.
- `created_at`: ISO timestamp of task creation.
- `updated_at`: ISO timestamp of last update.

Example `tasks.json`:
```json
[
  {
    "id": 1,
    "description": "Buy groceries",
    "status": "todo",
    "created_at": "2025-05-07T12:00:00.123456",
    "updated_at": "2025-05-07T12:00:00.123456"
  }
]
```

## Development
To extend or modify the CLI:
1. Edit `task_cli.py` to add new features or commands.
2. Update dependencies in `pyproject.toml` if needed.
3. Test changes:
   ```bash
   poetry run python task_cli.py --help
   ```

## Dedicatory
1. https://roadmap.sh/projects/task-tracker

## Contributing
Contributions are welcome! Please:
1. Fork the repository.
2. Create a feature branch.
3. Submit a pull request with a clear description of changes.

## License
This project is licensed under the MIT License.

## Contact
For questions or feedback, contact [Your Name] at [you@example.com].
