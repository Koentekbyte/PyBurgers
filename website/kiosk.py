from flask import Blueprint, render_template

kiosk = Blueprint("kiosk",__name__)

@kiosk.route("/")
def menu():
    return render_template("kiosk.html")