from flask import Blueprint

kitchenDisplay = Blueprint("kitchenDisplay ",__name__)

@kitchenDisplay.route("/")
def menu():
    return "View orders here"