from celery import shared_task
import random

@shared_task
def add(x, y):
    return x + y


@shared_task
def multiply(x, y):
    return x * y

@shared_task
def random_number_generator():
    return random.randint(1, 100)


@shared_task
def invokable_task(a):
    print(f"invokable task says: {a}")
