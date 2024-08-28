from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "PyBurgers.db"
def create_app():
    app = Flask(__name__)
    app.config["SECRET KEY"] = "UFEIFBEBFOEFBOBH" 
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    db.init_app(app)

    from .routes import routes
    from .kiosk import kiosk
    from .kitchenDisplay import kitchenDisplay
    from .status import status
    
    app.register_blueprint(routes,url_prefix="/")
    app.register_blueprint(kiosk,url_prefix="/kiosk")
    app.register_blueprint(kitchenDisplay ,url_prefix="/kitchenDisplay")
    app.register_blueprint(status, url_prefix="/status")
    
    from . import tables
      
    
    
    
    with app.app_context():
        db.create_all()

    return app




def populate_database():
        if db.keys():
            print("DB not empty")
    
        if not db.keys():
            print("DB is empty")