from flask import Blueprint, render_template, redirect
#from .tables import Orders,OrderItems,Menu,Progress

kiosk = Blueprint("kiosk",__name__)
itemsDict = {"PyThane":"/static/PyThane-icon.png","PyCheeseburger":"/static/burger-icon.png","PyChicken":"/static/PyChicken-icon.png","PyVeggie":"/static/PyVeggie-icon.png"}
@kiosk.route("/")
def menu():
    return redirect("burgers")
@kiosk.route("/burgers")
def burgers():
    return render_template("menu-burgers.html")
@kiosk.route("/sides")
def sides():
    return render_template("menu-sides.html")
@kiosk.route("/drinks")
def drinks():
    return render_template("menu-drinks.html")
@kiosk.route("/order")
def order():
    return render_template("menu-order.html")
@kiosk.route("/customise/<itemName>")
def customise(itemName):
   #menu_items = Menu.query.all()
    return render_template("menu-custom.html",customToken=[itemName,itemsDict[itemName]])
        


    