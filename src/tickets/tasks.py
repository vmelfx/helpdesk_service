from time import sleep

from config.celery import celery_app


@celery_app.task
def hello_task():
    sleep(7)
    print("Hello from Celery")
