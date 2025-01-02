from dcelery.celery_config import app
from celery import group

"""
from dcelery.celery_tasks.ex_error_handling_groups import run_tasks
run_tasks()
"""




@app.task(queue="tasks")
def my_error_groups(number):
    if number == 3  :
        raise ValueError("Value Error")
    return number *2


def handle_result(result):
    if result.successful():
        print(f"Result: {result.get()}")
    elif result.failed() and isinstance(result.result, ValueError):
        print(f"Value Error: {result.result}")    
    elif result.status == 'REVOKED':
        print(f"Task was revoked: {result.id}")


def run_tasks():
    task_group = group(
        my_error_groups.s(1),
        my_error_groups.s(2),
        my_error_groups.s(3),
        my_error_groups.s(4),
    )
    result_group = task_group.apply_async()
    
    for result in result_group.children:  # Use `.children` to get individual task results
        try:
            # Get the result or raise an exception for failed tasks
            result.get(disable_sync_subtasks=False)
        except Exception as e:
            # Handle task-specific exceptions
            print(f"Error occurred in task {result.id}: {e}")
        finally:
            handle_result(result)
