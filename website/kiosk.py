from flask import Blueprint, render_template, redirect, flash
from .tables import Orders,OrderItems,Menu
from . import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select
from flask import request


kiosk = Blueprint("kiosk",__name__)
itemsDict = {"PyThane":"/static/PyThane-icon.png","PyCheeseburger":"/static/burger-icon.png","PyChicken":"/static/PyChicken-icon.png","PyVeggie":"/static/PyVeggie-icon.png"}

currentRecord = 0

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


@kiosk.route("/order", methods =["GET", "POST"])
def order():
    global basket
    
    
    basket = db.session.query(
        OrderItems, Menu, Orders,
    ).filter(
        Orders.status == "pending",
    ).filter(
        OrderItems.orderID == Orders.orderID,
    ).filter(
        OrderItems.menuID == Menu.menuID,
    ).all()




    if not basket:
        basket="empty"
    
    return render_template("menu-order.html",basket=basket)


@kiosk.route("/customise/<itemName>")
def customise(itemName):
    global currentItem
    currentItem = itemName
    global menu_items_record
    menu_items_record = Menu.query.filter_by(itemName=itemName).first()
    currentRecord = Menu.query.filter_by(itemName=itemName).first()
    return render_template("menu-custom.html",customToken=menu_items_record)
        

@kiosk.route("/submit",  methods =["GET", "POST"])
def submit():
    global currentItem
    temp = 0
    modList = ""
    global menu_items_record
    if request.method == "POST":
       # getting input with name = fname in HTML form
       for i in menu_items_record.base_fixings.split(","):
            if "No" in i: #default option for topping is "No"
                j = request.form.get(i[2:]) #fetches the user choice for that specific topping, if it is extra/normal then it should appear as a mod: EX_Lettuce/ADD_Lettuce otherwise it should not be recorded as a mod
                if j == "1":
                    modList += f"ADD_{i[2:]},"
                elif j == "2":
                    modList += f"EXTRA_{i[2:]},"
                else:
                    pass
            elif menu_items_record.itemName=="Salad":
                j = request.form.get(i)
                if j == "0":
                    modList = "NO_Vinaigrette#"

            elif "No" not in i and menu_items_record.foodType=="burger": #default topping is normal
                j = request.form.get(i)
                if j == "2":
                    modList += f"EXTRA_{i},"
                elif j == "0":
                    modList += f"NO_{i},"
                else:
                    pass
            elif menu_items_record.foodType=="drinks":
                j = request.form.get(i)
                if j == "0":
                    modList = "Small#"
                elif j == "1":
                    modList = "Medium#"
                elif j == "2":
                    modList = "Large#"
                else:
                    pass
            
                #need to add way for drinks to be modded properly

            
    temp = 0
    #create a new order is there are no pending orders before (see if the last record in status, Progress is "pending")
    #add an entry to Orders with a null time, and an entry to Progress with the last orderID in Orders with a "pending" status
    lastQuery = Orders.query.filter_by(status="pending").first()
    if lastQuery == None:
        db.session.add(Orders(status="pending"))
        db.session.commit()
        qAdd = Orders.query.filter_by(status="pending").first()
        temp=qAdd.orderID
        qItem = Menu.query.filter_by(itemName=currentItem).first()
        db.session.add(OrderItems(orderID=qAdd.orderID,menuID=qItem.menuID,modifications=modList[0:-1]))
        db.session.flush()
        #db.session.add(Progress(orderID=qAdd.orderID,status="pending"))
    else:
        qAdd = Orders.query.filter_by(status="pending").first()
        temp=qAdd.orderID
        qItem = Menu.query.filter_by(itemName=currentItem).first()
        db.session.add(OrderItems(orderID=qAdd.orderID,menuID=qItem.menuID,modifications=modList[0:-1]))
        db.session.flush()
       # temp = f"{lastQuery.orderID}"
    db.session.commit()

    return redirect("order")
@kiosk.route("/confirm", methods=["GET","POST"])
def confirm():
    global basket
    
    db.session.commit()
    toDelete=0
    displayList = []
    if request.method == "POST":
        for order_item,menu_item,order in basket:
            
            if request.form.get(f"{order_item.itemID}-state") == "0":
               displayList.append(order_item.itemID)
                
                
                #db.session.delete(toDelete)
                #print("DELETED")
                #db.session.commit()
           # else:
                #print("PASSED")
                #pass
        for i in displayList:
            toDelete=OrderItems.query.filter_by(itemID=i).first()
            db.session.delete(toDelete)
            db.session.commit()
    db.session.commit()
    return redirect("order")      
            
        #pass
        #if request.method.
            

    
@kiosk.route("/payment",  methods =["GET", "POST"] )
def payment():
    global basket
    global statusNum
    redir = "success"
    if request.method == "POST":
        for order_item,menu_item,order in basket:
            
            if request.form.get(f"{order_item.itemID}-state") == "0":
                flash('Pending changes remaining!')
                redir="order"
                break
        #no pending items remaining confirmed
        #check off order
        db.session.commit()
        toUpdate = Orders.query.filter_by(status="pending").first()
        statusNum = toUpdate.orderID
        toUpdate.status="received"
        db.session.commit()
        
        
    return redirect(redir)
    
        #if 
@kiosk.route("/success")
def success():
    global statusNum
    return render_template("success.html",statusNum=statusNum)
@kiosk.route("/restart",methods=['GET', 'POST'])
def restart():
    global basket
    delList=[]
    #toRestart = Orders.query.filter_by(status="pending").first()
    if request.method == "POST":
        for order_item,menu_item,order in basket:
            
            
            delList.append(order_item.itemID)
                
                
                #db.session.delete(toDelete)
                #print("DELETED")
                #db.session.commit()
           # else:
                #print("PASSED")
                #pass
        for i in delList:
            toDelete=OrderItems.query.filter_by(itemID=i).first()
            db.session.delete(toDelete)
            db.session.commit()
    return redirect("burgers")