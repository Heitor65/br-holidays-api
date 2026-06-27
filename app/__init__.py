from flask import Flask
from flasgger import Swagger

def create_app():
    app=Flask(__name__)
    Swagger(app)
    from app.routes.main import main_bp
    app.register_blueprint(main_bp)
    return app