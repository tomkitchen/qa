import os
import sys

sys.path.append('/home/ubuntu/medivet/qa/')

os.environ['DJANGO_SETTINGS_MODULE'] = 'qa.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
