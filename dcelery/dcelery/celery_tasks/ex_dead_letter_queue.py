from celery import group
from dcelery.celery_config import app


"""
from dcelery.celery_tasks.ex_dead_letter_queue import run_task_group
run_task_group()
"""



app.conf.task_acks_late = True
app.conf.task_reject_on_worker_lost = True

app.task(queue="tasks")
def my_task(z):
    try:
        if z == 2:
            raise ValueError("Value Error")
    except Exception as e:
        handle_failed_task.apply_async(args=(z,str(e)))

@app.task(queue="dead_letter")
def handle_failed_task(z, exception):
    return "custom logic to process"

def run_task_group():
    task_group =group(my_task.s(1),my_task.s(2),my_task.s(3),my_task.s(4))
    task_group.apply_async()
