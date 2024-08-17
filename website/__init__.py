from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config["SECRET KEY"] = "ICTHYS" 

    from .routes import routes
    from .kiosk import kiosk
    from .kitchenDisplay import kitchenDisplay
    
    app.register_blueprint(routes,url_prefix="/")
    app.register_blueprint(kiosk,url_prefix="/kiosk")
    app.register_blueprint(kitchenDisplay ,url_prefix="/kitchenDisplay")
    return app