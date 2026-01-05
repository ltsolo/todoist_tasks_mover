from typing import Iterator
from datetime import date, timedelta
import os

from todoist_api_python.api import TodoistAPI, Task

TODOIST_API_KEY = api_key = os.getenv("TODOIST_API_KEY")

TASK_DEBUG_FILTER = "TTSTTS"

def main():
    api = TodoistAPI(TODOIST_API_KEY)
    tasks: Iterator[list[Task]] = api.get_tasks(limit=200)
    filtered_tasks: list[Task] = []
    for task_section in tasks:
        for task in task_section:
            if task.due:
                if task.due.date == date.today():
                    filtered_tasks.append(task)
    for task in filtered_tasks:
        if task.content == TASK_DEBUG_FILTER:
            print(f"task: {task.content} -- {task.due.date}")
            api.update_task(task.id, due_date=date.today() + timedelta(days=1))

if __name__ == "__main__":
    main()