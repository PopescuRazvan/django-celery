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
from dcelery.celery_tasks.ex_custom_task_class import my_task_custom_class
my_task_custom_class.delay()
"""

@app.task(queue="tasks")
def my_task_custom_class():
    try:
        raise ConnectionError("Connection Error")
    except ConnectionError:
        logging.error("Connection Error")
        raise ConnectionError()
    except ValueError:
        logging.error("Value Error")
        perform_specific_error_handling()        
    except Exception:
        logging.error("Unknown Error")
        notify_admin()
        perform_fallback_action()

def perform_specific_error_handling():
    #logic to handle specific error
    pass

def notify_admin():
    #logic to notify admin
    pass

def perform_fallback_action():
    #logic to perform fallback action
    pass