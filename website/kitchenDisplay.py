from flask import Blueprint,render_template, redirect
from .tables import Menu, OrderItems, Orders
from . import db
kitchenDisplay = Blueprint("kitchenDisplay",__name__)

@kitchenDisplay.route("/")
def kDisplay():
   
    orderDict = {}
    db.session.commit()
    orderIterator = Orders.query.filter_by(status="received").all()
    for i in orderIterator:
        relatedPackage = db.session.query(
        OrderItems, Menu
        ).filter(
        OrderItems.orderID == i.orderID,
        ).filter(
        OrderItems.menuID == Menu.menuID,
        ).all()

        orderDict[i.orderID] = relatedPackage

    #need to package all this into a dict, {1: }
    """
    1) iterate through received orders
    2) use their orderID to find related orderItems and Menu records
    3) add to dictionary as { 1 : [menu records, orderitems records], 2 : [menu records, orderitems records]}


    """

    return render_template("kitchen-display.html",orderDict=orderDict)

@kitchenDisplay.route("/finished/<name>")
def finished(name):
    
    db.session.commit()
    toUpdate = Orders.query.filter_by(orderID=name, status="received").first()
    toUpdate.status="finished"
    db.session.commit()
    return redirect("/kitchenDisplay")
    