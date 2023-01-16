from flask import current_app as app, session, redirect
from flask import Blueprint, jsonify, request
from flask_mysqldb import MySQL

api = Blueprint('api', __name__)
mysql = MySQL(app)

# sanity check route
@api.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@api.route('/listall', methods=['GET'])
def check():
    with mysql.connection.cursor() as cur:
        mysqlquery = '''select * from machines'''
        cur.execute(mysqlquery)
        results = cur.fetchall()
        print(results)
        return jsonify(results)

@api.route('/add_machine', methods=['POST'])
def add_machine():
    with mysql.connection.cursor() as cur:
        try:
            args = request.args
            mysqlquery = '''insert into machines(handle, location, status) values (%s, %s, %s)'''
            cur.execute(mysqlquery, (args.get("handle"), args.get("location"), args.get("status")))
            cur.connection.commit()
            return jsonify("Success!")
        except Exception as e:
            print(e)
            return jsonify("Failed: {{e}}")

@api.route("/delete_machine", methods=['POST'])
def delete_machine():
    with mysql.connection.cursor() as cur:
        try:
            args = request.args
            mysqlquery = '''delete from machines where id = %s'''
            cur.execute(mysqlquery, args.get('id'))
            cur.connection.commit()
            return "Success!"
        except Exception as e:
            return "Failed: {{e}}"

@api.route("/update_machine", methods=['POST'])
def update_machine():
    with mysql.connection.cursor() as cur:
        try:
            args = request.args
            mysqlquery = '''update machines set handle = %s, location = %s, status = %s where id = %s'''
            cur.execute(mysqlquery, (args.get("handle"), args.get("location"), args.get("status"), args.get("id")))
            cur.connection.commit()
            return "Success!"
        except Exception as e:
            return e