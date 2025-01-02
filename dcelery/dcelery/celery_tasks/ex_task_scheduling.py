from datetime import timedelta
from dcelery.celery_config import app

app.conf.beat_schedule = {
    'task1': {
        'task':'delcery.celery_tasks.ex_task_scheduling.task1',
        'schedule':timedelta(seconds=5),
    },
    'task2':{
        'task':'delcery.celery_tasks.ex_task_scheduling.task2',
        'schedule':timedelta(seconds=5),
    }
}

@app.task(queue="tasks")
def task1():
    print("Task 1 executed")


@app.task(queue="tasks")
def task2():
    print("Task 2 executed")