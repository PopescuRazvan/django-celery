from dcelery.celery_config import app
import logging

logging.basicConfig(filename="app.log", level=logging.ERROR,format='%(asctime)s %(levelname)s %(message)s')

"""
from dcelery.celery_tasks.ex_try_except import my_task_try_except
my_task_try_except.delay()
"""

@app.task(queue="tasks")
def my_task_try_except():
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