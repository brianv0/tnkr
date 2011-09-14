import os
import sys

sys.path= ['/sites/tnkr/home'] + sys.path
sys.path= ['/sites/tnkr'] + sys.path

from django.core.handlers.wsgi import WSGIHandler

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
application = WSGIHandler()
