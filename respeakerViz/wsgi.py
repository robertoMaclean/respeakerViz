"""
WSGI config for respeakerViz project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import sys
import site
import os

# Add the site-packages of the chosen virtualenv to work with
#site.addsitedir('/usr/share/.virtualenvs/respeakerVizEnv/lib/python3.5/site-packages')

# Add the app's directory to the PYTHONPATH
#sys.path.append('/var/www/html/voiceAnalyzer/respeakerViz')
#sys.path.append('var/www/html/voiceAnalyzer/respeakerViz/respeakerViz')
#for path in sys.path: print(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'respeakerViz.settings'

# Activate your virtual env
#activate_env=os.path.expanduser("/var/www/html/voiceAnalyzer/respeakerViz/respeakerVizEnv/bin/activate_this.py")
#execfile(activate_env, dict(__file__=activate_env))
#exec(open(activate_env).read(), dict(__file__=activate_env)) 

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
