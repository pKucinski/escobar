import sys, os
from django.core.wsgi import get_wsgi_application

sys.path.append(os.getcwd())
os.environ['DJANGO_SETTINGS_MODULE'] = "escobar.settings" 
application = get_wsgi_application()