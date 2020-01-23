# from __future__ import absolute_import, unicode_literals

import pymysql
#
from . celery import celery_app

pymysql.version_info = (1, 3, 13, "final", 0)

pymysql.install_as_MySQLdb()
#
__all__ = ('celery_app',)
