from celery import shared_task
from celery.decorators import task
from django.core.mail import send_mail
@task
def sendEmailToSetPassword(email, code):
    send_mail('Hello from Iskender.', str(code), 'onlinediaryputinbyte@yandex.ru', [email], fail_silently=False)
