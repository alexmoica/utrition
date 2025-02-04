from flask import Flask
from home.views import home_view


def create_app(config_file):
    build_app = Flask(__name__)  # Create application object
    build_app.config.from_pyfile(
        config_file
    )  # Configure application with settings file, not strictly necessary
    build_app.register_blueprint(
        home_view
    )  # Register url's so application knows what to do
    return build_app


if __name__ == "__main__":
    app = create_app("settingslocal.py")  # Create application with our config file
    app.run()  # Run our application
