import os
import sys

sys.path= ['/websoft'] + sys.path

from django.core.handlers.wsgi import WSGIHandler

os.environ['DJANGO_SETTINGS_MODULE'] = 'examples.settings'
application = WSGIHandler()
