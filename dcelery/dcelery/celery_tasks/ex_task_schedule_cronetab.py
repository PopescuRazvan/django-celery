from datetime import timedelta
from dcelery.celery_config import app
from celery.schedules import crontab

app.conf.beat_schedule = {
    'task1': {
        'task':'delcery.celery_tasks.ex_task_schedule_cronetab.task1',
        'schedule':crontab(minute='0-59/10',hour='0-5',day_of_week='mon'),
        #schedule':timedelta(seconds=5),
        'kwargs:':{'message':'The sum is'},
        'args':(5,10),
        'options':{'queue':'tasks','priority':5}
    },
    'task2':{
        'task':'delcery.celery_tasks.ex_task_schedule_cronetab.task2',
        'schedule':timedelta(seconds=5),
    }
}

@app.task(queue="tasks")
def task1(*args,**kwargs):
    print("Task 1 executed with args:", args, "and kwargs:", kwargs)


@app.task(queue="tasks")
def task2():
    print("Task 2 executed")





"""
* * * * * *  
| | | | | | |
| | | | | | + ---- Day of week (0 = Monday)
| | | | | +------ Month (0 = January)
| | | | +-------- Day of month (1 to 31)
| | | +---------- Hour (0 to 23)     
| | +------------ Minute (0 to 59)
"""

"""
* * * * *       #Run every minute
*/5 * * * *     #Run every 5 minutes
30 * * * *      #Run every hour at 30 minutes
0 9 * * *       #Run every day at 9 am
0 14 * * 1      #Run every Monday at 2 pm
0 0 1,15 * *    #Run every month on 1st and 15th at 12 am
0 20,23 * * 5   #Run every Friday at 8 pm and 11 pm
*/15 * * * *    #Run every 15 minutes
0 0 * * *       #Run every hour
0 12 * * MON    #Run every Monday at 12 am
0 0 1-7 * *     #Run every day from Monday to Sunday at 12 am
0 0/2 * * *     #Run every 2 hours
0 */6 * * *     #Run every 6 hours
0 0-8/2 * * *   #Run every 2 hours from 12 am to 8 am 
0 0,12 * * *    #Run every day at 12 am and 12 pm
0 0 * * 0       #Run every Sunday at 12 am
0 0 1 1 *       #Run every January 1st at 12 am
0 0 1 1 MON     #Run every January 1st at 12 am on Monday
"""


