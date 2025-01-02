from datetime import timedelta
from dcelery.celery_config import app

app.conf.beat_schedule = {
    'task1': {
        'task':'delcery.celery_tasks.ex_task_scheduling_customization.task1',
        'schedule':timedelta(seconds=5),
        'kwargs:':{'message':'The sum is'},
        'args':(5,10),
        'options':{'queue':'tasks','priority':5}
    },
    'task2':{
        'task':'delcery.celery_tasks.ex_task_scheduling_customization.task2',
        'schedule':timedelta(seconds=5),
    }
}

@app.task(queue="tasks")
def task1(*args,**kwargs):
    print("Task 1 executed with args:", args, "and kwargs:", kwargs)


@app.task(queue="tasks")
def task2():
    print("Task 2 executed")