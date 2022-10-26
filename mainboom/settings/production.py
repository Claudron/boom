import os
from .base import *
import dj_database_url


DEBUG = False
# SECRET_KEY = 'nu05%qz)1%^d4lb0kzf%@a@!t$kdi85ajp9elxqqajty3#$c3q'
# ALLOWED_HOSTS = ['localhost', .....]


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = {
#     'default': dj_database_url.config(
#         default='postgres://boomdb_user:CiFUt0yuQWy8jqyvWPkkhj0kbdULDgBB@dpg-cdal3782i3mnn0sl04o0-a:5432/boomdb',
#         conn_max_age=600
#     )
# }




# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'boomdb',
#         'USER': 'boomdb_user',
#         'PASSWORD': 'CiFUt0yuQWy8jqyvWPkkhj0kbdULDgBB',
#         'HOST': 'CiFUt0yuQWy8jqyvWPkkhj0kbdULDgBB@dpg-cdal3782i3mnn0sl04o0-a/boomdb',
#         'PORT': '5432',
#     }
# }

try:
    from .local import *
except ImportError:
    pass
