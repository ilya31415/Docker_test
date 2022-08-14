from multiprocessing import cpu_count
from os import environ

def max_workers():
    return cpu_count()


bind = '127.0.0.1:8000'
max_requests = 1000
worker_class = 'gevent'
workers = max_workers()

env = {
    'DJANGO_SETTINGS_MODULE': 'stocks_products.settings'
}

reload = True
name = 'project_django'