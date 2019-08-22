'''
DBCONFIG = {}

DBCONFIG['default'] = {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'huronshop',
    'USER': 'postgres',
    'PASSWORD': 'admin',
    'HOST': 'localhost',
    'PORT': 5432, 
}
'''
import dj_database_url
from decouple import config

DBCONFIG ={
    'default': dj_database_url.config(
        default = config('DATABASE_URL')
    )
}