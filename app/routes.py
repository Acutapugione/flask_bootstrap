from flask import render_template, request
from sqlmodel import select
from . import app, Post, Config


@app.get("/")
def index():
    items = Config.SESSION.scalars(select(Post)).all()
    return render_template("index.html", items=items)


@app.get("/posts")
def post_view():
    item_id = int(request.args.get("item_id"))
    item = Config.SESSION.get_one(Post, item_id)
    item = item.model_dump()
    return render_template("view.html", item=item)
