"""root of application"""

from flask import Flask
from .db import Config, Post


Config.restart_db()
app = Flask(
    __name__,
)
# app2 = Flask(
#     "BackendAPP",
# )


# @app2.get("/")
# def index():
#     return "What you think you are doing here?"


app.secret_key = r"M?:/~;Zph\]@*v~!TuV\6X[BNT%&6KdV"

from . import routes
