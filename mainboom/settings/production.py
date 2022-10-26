import os
from .base import *
import dj_database_url

DEBUG = False

DATABASES = {
    'default': dj_database_url.config(
        default=os.environ["DATABASE_URL"],
        conn_max_age=600
    )
}


