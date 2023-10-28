import multiprocessing
import os
from string import Template
from typing import Literal

import gevent

import app


def get_mode() -> Literal["development", "production"]:
    _mode = os.environ.get('MODE')
    if _mode is None:
        return "production"
    else:
        return "development"


mode = get_mode()

wsgi_app = Template('$app:$fn()').safe_substitute(app=app.__name__, fn=app.create_app.__name__)
bind = "127.0.0.1:8000"

"""worker"""
workers: int = 1 if mode == 'development' else multiprocessing.cpu_count() * 2 + 1
worker_class: str = gevent.__name__
timeout: int = 30 if mode == 'development' else 10
max_requests: int = 0 if mode == 'development' else 1200

"""logging"""
loglevel: str = 'debug' if mode == 'development' else 'info'
accesslog: str = '-'
# noinspection SpellCheckingInspection
errorlog: str = '-'

"""development"""
reload = mode == 'development'

"""Server Mechanics"""
preload_app = mode == 'production'
