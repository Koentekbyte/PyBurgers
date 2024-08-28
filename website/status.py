from flask import Blueprint

status = Blueprint("status",__name__)

@status.route("/")
def home():
    return "View order status here"