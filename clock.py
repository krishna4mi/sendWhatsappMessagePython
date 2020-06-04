# from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler
from love_honey import appLove


def job_function():
    print("Hello World")

sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(appLove, 'interval', seconds=2)

sched.start()