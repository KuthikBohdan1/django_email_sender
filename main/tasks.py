from celery import shared_task
from email_sender.celery import app
import time
from django.http import JsonResponse
from celery.result import AsyncResult
@app.task()
def my_sum(a, b):
    return a + b

@app.task()
def err(request, exc, traceback):
    print("task_error" + str(exc))
    # print('Task {0} raised exception: {1!r}\n{2!r}'.format(request.id, exc, traceback))


# @app.task()
# def see_status(task_id):
#     result = AsyncResult(task_id).info
#     if result['progress']:
#         progress = result['progress']
#     else:
#         progress = "100"
#     return progress


@app.task(bind=True)
def proces(self):
    self.update_state(state="PROGRESS", meta={'progress': 30})
    time.sleep(10)
    self.update_state(state="PROGRESS", meta={'progress': 50})
    time.sleep(10)
    self.update_state(state="PROGRESS", meta={'progress': 90})
    time.sleep(10)
    self.update_state(state="PROGRESS", meta={'progress': 100})
    time.sleep(5)
    return 'hello world: %i' 