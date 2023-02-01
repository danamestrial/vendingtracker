import os
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from flaskext.mysql import MySQL

mysql = MySQL()


def create_app(env_path: str = None) -> Flask:
    """To Create a new instance of App."""
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*", "send_wildcard": "False"}})

    dotenv_path = Path(env_path if env_path else ".env")
    load_dotenv(override=True, dotenv_path=dotenv_path)

    app.config["MYSQL_DATABASE_USER"] = os.getenv("USERNAME")
    app.config["MYSQL_DATABASE_PASSWORD"] = os.getenv("PASSWORD")
    app.config["MYSQL_DATABASE_DB"] = os.getenv("DB")
    app.config["MYSQL_DATABASE_HOST"] = os.getenv("HOST")

    mysql.init_app(app)

    with app.app_context():
        from routes.items_routes import item
        from routes.machines_routes import machine
        from routes.stock_routes import stock

        app.register_blueprint(machine)
        app.register_blueprint(item)
        app.register_blueprint(stock)

    return app


current_app = create_app()

if __name__ == "__main__":
    current_app.run(debug=True)
