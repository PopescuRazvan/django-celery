from dcelery.celery_config import app
import sys

"""
from dcelery.celery_tasks.ex_linking_result_callbacks import run_task
run_task()
"""

@app.task(queue="tasks")
def long_run_task():
    raise ValueError("Value Error in long run task")


def run_task():
    long_run_task.apply_async(link=[process_task_result.s()],link_error=[error_handler.s()])

@app.task(queue="tasks")
def error_handler(task_id,exec,traceback):
    sys.stdout.write(">>>>")
    sys.stdout.write(str(exec))
    sys.stdout.write(">>>>")
    sys.stdout.flush()



@app.task(queue="tasks")
def process_task_result(task_result):
    sys.stdout.write("process task results")
    sys.stdout.flush()