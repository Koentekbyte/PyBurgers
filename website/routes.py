from flask import Blueprint, redirect

routes = Blueprint("routes",__name__)

@routes.route("/")
def home():
    return redirect("/kiosk")