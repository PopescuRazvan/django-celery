from dcelery.celery_config import app
import logging
from celery import Task

logging.basicConfig(filename="app.log", level=logging.ERROR,format='%(asctime)s %(levelname)s %(message)s')

class CustomTaskClass(Task):
    def on_failure(self, exc, task_id, args, kwargs, einfo):
        if isinstance(exc, ConnectionError):
            logging.error("Connection Error -class")
        else:
            print('{0!r} failed: {1!r}'.format(task_id, exc))



app.Task = CustomTaskClass


"""
from dcelery.celery_tasks.ex_auto_retry import my_task_auto_retry
my_task_auto_retry.delay()
"""

@app.task(queue="tasks" , autoretry_for=(ConnectionError,), default_retry_delay=5, retry_kwargs={'max_retries': 5})
def my_task_auto_retry():
    raise ConnectionError("Connection Error")
    return