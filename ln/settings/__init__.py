"""
Django settings for ln project.

Generated by 'django-admin startproject' using Django 1.10.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

from ln.settings.main import *

if str(os.environ.get('IS_LOCAL', 1)):
    from ln.settings.local import *
else:
    from ln.settings.prod import *

