"""
WSGI config for diary project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

# import os
#
# from django.core.wsgi import get_wsgi_application
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'diary.settings')
#
# application = get_wsgi_application()

import os, sys

path='/var/www/html/diaryDjango'

if path not in sys.path:
  sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'diary.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
