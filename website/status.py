from flask import Blueprint, redirect, render_template
from .tables import OrderItems, Orders, Menu
from . import db

status = Blueprint("status",__name__)

@status.route("/")
def sDisplay():
    displayOrders = Orders.query.filter((Orders.status == 'received') | (Orders.status == 'finished')).all()


    return render_template("statusBoard.html",displayOrders=displayOrders)
@status.route("/collected/<name>")
def collected(name):

    orderToDelete=Orders.query.filter_by(orderID=name,status="finished").first()
    itemsToDelete=OrderItems.query.filter_by(orderID=orderToDelete.orderID).all()

    for i in itemsToDelete:
        db.session.delete(i)
    db.session.delete(orderToDelete)
    db.session.commit()

    return redirect("/status")