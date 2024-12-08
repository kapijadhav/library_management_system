from flask import Flask

def create_app():
    app = Flask(__name__)

    # Import the views and register the API blueprint
    from .views import api
    app.register_blueprint(api)

    return app
