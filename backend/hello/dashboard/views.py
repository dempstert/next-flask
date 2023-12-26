from flask import Blueprint, render_template
from sqlalchemy import text

from hello.extensions import db
from hello.initializers import redis

dash = Blueprint("dash", __name__, template_folder="templates", url_prefix="/up")


@dash.get("/")
def index():
    return ""

@dash.get("/reports")
def reports():
    return render_template(
        "page/reports.html",
        var="123"
    )
    return "reporting..."

@dash.get("/databases")
def databases():
    return "123"
    redis.ping()
    with db.engine.connect() as connection:
        connection.execute(text("SELECT 1"))
    return ""

@dash.get("/app")
def dashb():
    return render_template(
        "page/page.html"
    )