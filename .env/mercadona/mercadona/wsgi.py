"""
WSGI config for mercadona project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mercadona.settings')

application = get_wsgi_application()
<<<<<<< HEAD
=======


#-----Fly.io
from dotenv import load_dotenv
#Load environment variables from file
project_folder = os.path.expanduser('../mercadona')  # adjust as appropriate
load_dotenv(os.path.join(project_folder, '.env'))
>>>>>>> e3da257 (Init Mercadona promo app)