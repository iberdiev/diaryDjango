from celery import shared_task
from celery.decorators import task
from django.core.mail import send_mail
import datetime
from . import models

@shared_task
def sendEmailToSetPassword(email, code):
    send_mail('Hello from Iskender.', str(code), 'onlinediaryputinbyte@yandex.ru', [email], fail_silently=False)

@shared_task
def periodicPrintHelloWorld():
    print("Hello World")

@shared_task
def duplicateTodaysLessonsToNextWeek():
    today = datetime.date.today()
    oneWeekLater = today + datetime.timedelta(days=7)
    todaysLessons = models.Timetable.objects.filter(date=today)
    for lesson in todaysLessons:
        futureLesson = models.Timetable.objects.filter(date=oneWeekLater, startTime=lesson.startTime)
        if len(futureLesson) is 0:
            lessonToCreate = lesson
            lessonToCreate.date, lessonToCreate.pk  = oneWeekLater, None
            lessonToCreate.save()
