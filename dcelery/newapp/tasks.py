from celery import shared_task
import time
from django.core.management import call_command
# @shared_task
# def task1():
#     return


# @shared_task
# def task2():
#     return


@shared_task
def management_command(queue='tasks'):
    call_command('test_command.py')


# @shared_task(task_rate_limit='1/m')
# def tp1(queue='celery'):
#     time.sleep(3)
#     return

# @shared_task
# def tp2(queue='celery:1'):
#     time.sleep(3)
#     return


# @shared_task
# def tp3(queue='celery:2'):
#     time.sleep(3)
#     return

# @shared_task
# def tp4(queue='celery:3'):
#     time.sleep(3)
#     return


# example of task group run inside of docker
# from celery import group
# from newapp.tasks import tp1,tp2,tp3,tp4
# task_group = group(tp1.s(),tp2.s(),tp3.s(),tp4.s())
# task_group.apply_async()


#example of task  chain
# from celery import chain
# from newapp.tasks import tp1,tp2,tp3,tp4
# task_chain = chain(tp1.s(),tp2.s(),tp3.s(),tp4.s())
# task_chain.apply_async()


#example of task  inspect
#celery inspect active
#celery inspect active_queues