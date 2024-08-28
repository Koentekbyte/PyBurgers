from . import db

class Orders(db.Model):
    __tablename__ = 'Orders'
    orderID = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime, nullable=False)

class OrderItems(db.Model):
    __tablename__ = 'Orderitems'
    itemID = db.Column(db.Integer, primary_key=True)
    orderID = db.Column(db.Integer, db.ForeignKey('Orders.orderID'), nullable=False)
    menuID = db.Column(db.Integer, db.ForeignKey('Menu.menuID'), nullable=False)
    modifications = db.Column(db.String(255))

class Progress(db.Model):
    __tablename__ = 'Progress'
    progressID = db.Column(db.Integer, primary_key=True)
    orderID = db.Column(db.Integer, db.ForeignKey('Orders.orderID'), nullable=False)
    status = db.Column(db.String(50), nullable=False)

class Menu(db.Model):
    __tablename__ = 'Menu'
    menuID = db.Column(db.Integer, primary_key=True)
    itemName = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))
    base_fixings = db.Column(db.String(255))
    price = db.Column(db.Float, nullable=False)
    picture = db.Column(db.String(255))