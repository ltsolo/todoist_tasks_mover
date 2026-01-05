from datetime import date, timedelta
import os

from todoist_api_python.api import TodoistAPI, Task

TODOIST_API_KEY = api_key = os.getenv("TODOIST_API_KEY")

def get_today_tasks(api: TodoistAPI) -> list[Task]:
    tasks = api.get_tasks(limit=200)
    filtered_tasks: list[Task] = []
    for task_section in tasks:
        for task in task_section:
            if task.due:
                if task.due.date == date.today():
                    filtered_tasks.append(task)
    return filtered_tasks

def move_tasks(api: TodoistAPI, tasks: list[Task]) -> None:
    for task in tasks:
        print(f"Moving task: {task.content}")
        api.update_task(task.id, due_date=date.today() + timedelta(days=1))

def process_tasks(api: TodoistAPI) -> None:
    today_tasks = get_today_tasks(api)
    move_tasks(api, today_tasks)

def main():
    api = TodoistAPI(TODOIST_API_KEY)
    process_tasks(api)

if __name__ == "__main__":
    main()