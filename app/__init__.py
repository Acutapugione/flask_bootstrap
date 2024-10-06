"""root of application"""

from flask import Flask
from .db import Config, Post


Config.restart_db()
app = Flask(
    __name__,
)


from . import routes
