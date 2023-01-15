from flask import Flask, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS
from dotenv import load_dotenv
import os

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)

app.config['MYSQL_HOST'] = os.getenv('HOST')
app.config['MYSQL_USER'] = os.getenv('USERNAME')
app.config['MYSQL_PASSWORD'] = os.getenv('PASSWORD')
app.config['MYSQL_DB'] = os.getenv('DB')
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/listall', methods=['GET'])
def check():
    with mysql.connection.cursor() as cur:
        mysqlquery = '''select * from machines'''
        cur.execute(mysqlquery)
        results = cur.fetchall()
        print(results)
        return jsonify(results)

@app.route("/add_machine/<handle>/<location>", methods=['POST'])
@app.route('/add_machine/<handle>/<location>/<status>', methods=['POST'])
def add_machine(handle: str, location: str, status: int = 0):
    with mysql.connection.cursor() as cur:
        try:
            mysqlquery = '''insert into machines(handle, location, status) values (%s, %s, %s)'''
            cur.execute(mysqlquery, (handle, location, status))
            cur.connection.commit()
            return jsonify("Success!")
        except Exception as e:
            print(e)
            return jsonify("Failed: {{e}}")

@app.route("/delete_machine/<id>", methods=['POST'])
def delete_machine(id: int):
    with mysql.connection.cursor() as cur:
        try:
            mysqlquery = '''delete from machines where id = %s'''
            cur.execute(mysqlquery, id)
            cur.connection.commit()
            return "Success!"
        except Exception as e:
            return "Failed: {{e}}"

@app.route("/update_machine/<id>/<handle>/<location>/<status>", methods=['POST'])
def update_machine(id: int, handle: str, location: str, status: int = 0):
    with mysql.connection.cursor() as cur:
        try:
            mysqlquery = '''update machines set handle = %s, location = %s, status = %s where id = %s'''
            cur.execute(mysqlquery, (handle, location, status, id))
            cur.connection.commit()
            return "Success!"
        except Exception as e:
            return e

if __name__ == '__main__':
    app.run(debug=True)