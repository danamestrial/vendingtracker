from flask import Blueprint, jsonify, request
from .utils import *

machine = Blueprint('machine', __name__)

# sanity check route
@machine.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@machine.route('/list-all-machines', methods=['GET'])
def list_all():
    with mysql.connection.cursor() as cur:
        mysqlquery = '''select * from machines'''
        cur.execute(mysqlquery)
        results = cur.fetchall()
        print(results)
        return jsonify(results)

@machine.route('/add-machine', methods=['POST'])
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

@machine.route("/delete-machine", methods=['POST'])
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

@machine.route("/update-machine", methods=['POST'])
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