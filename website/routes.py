from flask import Blueprint, redirect
from flask_sqlalchemy import SQLAlchemy
from . import db
from .tables import OrderItems, Orders, Menu


routes = Blueprint("routes",__name__)

@routes.route("/")
def home():
    return redirect("/kiosk")

#Initial population of the database

"""


@routes.route("/populate")
def populate():

    items = [
        
        Menu(itemName="Grimace Shake",description="Don't sue me McDonalds :(",base_fixings="NoGrimace,NoChocolate,NoVanilla",price=3.19,picture="/static/drinks-icon.png", foodType="drinks"),
        Menu(itemName="Chocolate Shake",description="Decadent and rich",base_fixings="NoGrimace,NoChocolate,NoVanilla",price=2.99,picture="/static/drinks-icon.png", foodType="drinks"),
        Menu(itemName="Cheese Bites",description="an explosion of cheese",base_fixings="NoGrimace,NoChocolate,NoVanilla",price=2.50,picture="/static/drinks-icon.png", foodType="sides"),
        Menu(itemName="Salad",description="Fresh and organic",base_fixings="NoGrimace,NoChocolate,NoVanilla",price=3.25,picture="/static/drinks-icon.png", foodType="sides"),
    ]

    
    db.session.bulk_save_objects(items)  # Bulk insert
    db.session.commit()  # Commit to save changes
    return "Menu items added to the database!"

 
        Menu(itemName="PyThane",description="The one burger to rule them all",base_fixings="Mustard,Ketchup,Mayo,Lettuce,Pickles,Cheese",price=9.99,picture="/static/PyThane-icon.png",foodType="burger"),
        Menu(itemName="PyCheeseburger",description="Classic handmade cheeseburger",base_fixings="Mustard,Ketchup,NoMayo,NoLettuce,Pickles,NoCheese",price=6.99,picture="/static/burger-icon.png",foodType="burger"),
        Menu(itemName="PyChicken",description="A rustic chicken sandwich",base_fixings="NoMustard,NoKetchup,Mayo,Lettuce,NoPickles,NoCheese",price=7.99,picture="/static/PyChicken-icon.png", foodType="burger"),
        Menu(itemName="PyVeggie",description="Flame-grilled vegetable goodness",base_fixings="Mustard,Ketchup,NoMayo,Lettuce,Pickles,NoCheese",price=6.99,picture="/static/PyVeggie-icon.png", foodType="burger"),
        Menu(itemName="Fries",description="Skin-on & fried in beef tallow",base_fixings="NoKetchup,NoMayo,NoBBQ",price=2.99,picture="/static/fries-icon.png", foodType="sides"),
        Menu(itemName="Nuggets",description="10pc box of crispy chicken nuggets",base_fixings="NoKetchup,NoMayo,NoBBQ",price=3.99,picture="/static/fries-icon.png", foodType="sides"),
        Menu(itemName="PyPsi",description="Crafted with our ginger and kola nut extract",base_fixings="Ice",price=2.99,picture="/static/drinks-icon.png", foodType="drinks"),
         

"""