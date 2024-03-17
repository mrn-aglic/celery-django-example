# Celery Django example
This repo contains a basic example of Django+Celery
for the purpose of exploring the admin panel options
related to periodic task management. 

Before accessing the admin panel, you need to create
a superuser:
```shell
docker exec -it celery-django-web-1 python manage.py createsuperuser
```
where celery-django-web-1 is the container name.

Assign a username and email.

Aftwerwards, visit and login to:
```shell
http://localhost:8000/admin
```