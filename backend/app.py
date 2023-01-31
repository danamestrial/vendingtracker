from flask import Flask
from flask_cors import CORS
import os


def create_app():
    app = Flask(__name__)
    CORS(app, resources={r'/*': {'origins': '*'}})

    app.config['MYSQL_HOST'] = os.getenv('HOST')
    app.config['MYSQL_USER'] = os.getenv('USERNAME')
    app.config['MYSQL_PASSWORD'] = os.getenv('PASSWORD')
    app.config['MYSQL_DB'] = os.getenv('DB')
    app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

    with app.app_context():
        from routes.machines_routes import machine
        from routes.items_routes import item
        from routes.stock_routes import stock
        app.register_blueprint(machine)
        app.register_blueprint(item)
        app.register_blueprint(stock)

    return app


current_app = create_app()

if __name__ == '__main__':
    current_app.run(debug=True)
