from . import db

class Orders(db.Model):
    __tablename__ = 'Orders'
    orderID = db.Column(db.Integer, primary_key=True,autoincrement=True)
    status = db.Column(db.String(50), nullable=False) #pending, received, finished

class OrderItems(db.Model):
    __tablename__ = 'Orderitems'
    itemID = db.Column(db.Integer, primary_key=True,autoincrement=True)
    orderID = db.Column(db.Integer, db.ForeignKey('Orders.orderID'), nullable=False)
    menuID = db.Column(db.Integer, db.ForeignKey('Menu.menuID'), nullable=False)
    modifications = db.Column(db.String(255))


class Menu(db.Model):
    __tablename__ = 'Menu'
    menuID = db.Column(db.Integer, primary_key=True,autoincrement=True)
    itemName = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))
    base_fixings = db.Column(db.String(255))
    price = db.Column(db.Float, nullable=False)
    picture = db.Column(db.String(255))
    foodType = db.Column(db.String(255))
