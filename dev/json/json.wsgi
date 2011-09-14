import os
import sys

sys.path= ['/websoft/json'] + sys.path

from django.core.handlers.wsgi import WSGIHandler

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
application = WSGIHandler()
