from flask import Blueprint, redirect
from flask_sqlalchemy import SQLAlchemy
from . import db
from .tables import OrderItems, Orders, Menu, Progress


routes = Blueprint("routes",__name__)

@routes.route("/")
def home():
    return redirect("/kiosk")

"""
@routes.route("/populate")
def populate():

    items = [
        Menu(itemName="PyThane",description="The one burger to rule them all",base_fixings="Mustard,Ketchup,Mayo,Lettuce,Pickles,Cheese",price=9.99,picture="/static/PyThane-icon.png"),
        Menu(itemName="PyCheeseburger",description="Our signature, a classic handmade cheeseburger",base_fixings="Mustard,Ketchup,NoMayo,NoLettuce,Pickles,NoCheese",price=6.99,picture="/static/burger-icon.png"),
        Menu(itemName="PyChicken",description="A rustic chicken sandwich, marinated in buttermilk and fried 'til golden brown",base_fixings="NoMustard,NoKetchup,Mayo,Lettuce,Pickles,NoCheese",price=7.99,picture="/static/PyChicken-icon.png"),
        Menu(itemName="PyVeggie",description="You won't have to compromise on taste for the sake of your moral compass with our irresistible take on a vegetable burger",base_fixings="Mustard,Ketchup,NoMayo,Lettuce,Pickles,NoCheese",price=6.99,picture="/static/PyVeggie-icon.png"),
        Menu(itemName="Fries",description="Traditional skin-on beef tallow fried chips, served with up 3 house made sauces",base_fixings="",price=2.99,picture="/static/fries-icon.png"),
        Menu(itemName="Nuggets",description="10pc box of crispy chicken nuggets, served with up to 3 house made sauces",base_fixings="",price=3.99,picture="/static/fries-icon.png"),
        Menu(itemName="PyPsi",description="Flavoured with ginger and kola nut extract, served with/out ice",base_fixings="Ice",price=2.99,picture="/static/drinks-icon.png"),
        Menu(itemName="Milkshake",description="Creamy ice cream, blended with fresh ice and full fat milk",base_fixings="",price=3.99,picture="/static/drinks-icon.png")
    ]

    
    db.session.bulk_save_objects(items)  # Bulk insert
    db.session.commit()  # Commit to save changes
    return "Menu items added to the database!"
"""