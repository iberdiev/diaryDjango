import datetime, os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "diary.settings")
django.setup()

from main_api import models

users = models.CustomUser.objects.all()
for user in users:
    user.set_password(user.username)
    user.save() 

