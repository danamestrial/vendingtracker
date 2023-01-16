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
        from routes.routes import api
        app.register_blueprint(api)

    return app

current_app = create_app()

if __name__ == '__main__':
    current_app.run(debug=True)