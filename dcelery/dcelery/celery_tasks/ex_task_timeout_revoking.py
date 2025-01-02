import sys 
from time import sleep
from  dcelery.celery_config import app

"""
from dcelery.celery_tasks.ex_task_timeout_revoking import long_run_task
long_run_task()

from dcelery.celery_tasks.ex_task_timeout_revoking import execute_task_example()
execute_task_example()
"""

@app.task(time_limit=5,queue="tasks")
def long_run_task():
    sleep(6)
    return "TASK COMPLETED"


@app.task(queue="tasks",bind=True)
def process_task_result(self,task_result):
    if task_result is None :
        print("Task has been revoked")
    else :
        print("Task has completed with result : ", task_result) 


def execute_task_example():
    result = long_run_task.delay()
    try :
        task_result = result.get(timeout= 3)
    except TimeoutError :
        print("Task has timed out")
    except Exception as e :
        print("Task failed with exception : ", e)
    
    task = long_run_task.delay()


    task.revoke(terminate=True)
    sleep(3)
    sys.stdout.write(task.status)

    if task.status == 'REVOKED' :
        process_task_result.delay(None)
    else:
        process_task_result.delay(task_result)