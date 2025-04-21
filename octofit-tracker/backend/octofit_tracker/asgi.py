"""
ASGI config for octofit_tracker project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
=======
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
>>>>>>> 2dba9b8 (Set up OctoFit Tracker project structure and backend environment)
"""

import os

from django.core.asgi import get_asgi_application

<<<<<<< HEAD
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
=======
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "octofit_tracker.settings")
>>>>>>> 2dba9b8 (Set up OctoFit Tracker project structure and backend environment)

application = get_asgi_application()
