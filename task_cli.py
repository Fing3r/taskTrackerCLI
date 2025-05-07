import click
import json
import os
from datetime import datetime

#File to store tasks
TASK_FILE = 'tasks.json'

#Task Statuses
STATUS_TODO = 'TODO'
STATUS_IN_PROGRESS = 'IN_PROGRESS'
STATUS_DONE = 'DONE'


#def JSON file to store tasks
def load_tasks():
    """Load tasks from the JSON file."""
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, 'r') as f:
        return json.load(f)
    
def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(TASK_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

def get_next_id(tasks):
    """Get the next available ID for a new task."""
    return max((task["id"] for task in tasks), default=0) + 1

########################
@click.group()
def cli():
    """Task Management CLI"""
    pass

@cli.command()
@click.argument("description")
def add(description):
    """Add a new task."""
    tasks = load_tasks()
    task = {
        "id": get_next_id(tasks),
        "description": description,
        "status": STATUS_TODO,
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat()
    }
    tasks.append(task)
    save_tasks(tasks)
    click.echo(f"Task added successfully (ID: {task['id']})")

@cli.command()
@click.argument("task_id", type=int)
@click.argument("description")
def update(task_id, description):
    """Update a task's description."""
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = description
            task["updated_at"] = datetime.now().isoformat()
            save_tasks(tasks)
            click.echo(f"Task {task_id} updated successfully")
            return
    click.echo(f"Task {task_id} not found")

@cli.command()
@click.argument("task_id", type=int)
def delete(task_id):
    """Delete a task."""
    tasks = load_tasks()
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks.pop(i)
            save_tasks(tasks)
            click.echo(f"Task {task_id} deleted successfully")
            return
    click.echo(f"Task {task_id} not found")

@cli.command(name="mark-in-progress")
@click.argument("task_id", type=int)
def mark_in_progress(task_id):
    """Mark a task as in-progress."""
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = STATUS_IN_PROGRESS
            task["updated_at"] = datetime.now().isoformat()
            save_tasks(tasks)
            click.echo(f"Task {task_id} marked as in-progress")
            return
    click.echo(f"Task {task_id} not found")

@cli.command(name="mark-done")
@click.argument("task_id", type=int)
def mark_done(task_id):
    """Mark a task as done."""
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = STATUS_DONE
            task["updated_at"] = datetime.now().isoformat()
            save_tasks(tasks)
            click.echo(f"Task {task_id} marked as done")
            return
    click.echo(f"Task {task_id} not found")

@cli.command(name="list")
@click.argument("status", required=False, type=click.Choice([STATUS_TODO, STATUS_IN_PROGRESS, STATUS_DONE]))
def list_tasks(status):
    """List tasks, optionally filtered by status."""
    tasks = load_tasks()
    if status:
        tasks = [task for task in tasks if task["status"] == status]
    
    if not tasks:
        click.echo("No tasks found")
        return
    
    for task in tasks:
        click.echo(f"ID: {task['id']} | Status: {task['status']} | Description: {task['description']} | Created: {task['created_at']} | Updated: {task['updated_at']}")

if __name__ == "__main__":
    cli()
