from celery import shared_task
import time

@shared_task
def test_task():
    print("Начинаю задачу...")
    time.sleep(5)
    print("Задача выполнена!")
    return "Готово!"
