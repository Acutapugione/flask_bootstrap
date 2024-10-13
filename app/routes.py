from flask import redirect, render_template, request, url_for, flash, Response

from sqlmodel import select
from dataclasses import dataclass
from . import app, Post, Config


@app.get("/")
def index():
    items = Config.SESSION.scalars(select(Post)).all()
    return render_template("index.html", items=items)


@app.get("/posts")
def post_view():
    item_id = int(request.args.get("item_id", 0))
    item = Config.SESSION.get_one(Post, item_id)
    item = item.model_dump()
    return render_template("view.html", item=item)


@dataclass
class PostForm:
    title: str
    content: str


@app.get("/posts/create")
def post_form():
    return render_template("form.html", item=PostForm("", "").__dict__)


@app.post("/posts/create")
def post_create():
    form_data = request.form
    item = Post(
        content=form_data.get("content"),
        title=form_data.get("title"),
    )
    if item.title and item.content:
        Config.SESSION.add(item)
        Config.SESSION.commit()
        print(f"{form_data=}")
        return redirect(url_for(index.__name__))

    flash(category="error", message="Заповніть форму")
    resp = Response(
        render_template("form.html", item=PostForm("", "").__dict__), status=422
    )

    return resp
