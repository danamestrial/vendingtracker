from flask import Blueprint, jsonify, request
from .utils import *

item = Blueprint('item', __name__)

@item.route("/list-all-items", methods=['GET'])
def list_all():
    with mysql.connection.cursor() as cur:
        mysqlquery = '''select * from items'''
        cur.execute(mysqlquery)
        results = cur.fetchall()
        print(results)
        return jsonify(results)

@item.route("/add-item", methods=['POST'])
def add_item():
    with mysql.connection.cursor() as cur:
        args = request.args
        mysqlquery = '''insert into items(name) values(%s)'''
        cur.execute(mysqlquery, (args.get('name'),))
        cur.connection.commit()
    return status(True)

@item.route("/remove-item", methods=['POST'])
def remove_item():
    with mysql.connection.cursor() as cur:
        args = request.args
        mysqlquery = '''delete from items where id = %s'''
        cur.execute(mysqlquery, args.get('id'))
        cur.connection.commit()
    return status(True)

@item.route("/update-item", methods=['POST'])
def update_item():
    with mysql.connection.cursor() as cur:
        args = request.args
        mysqlquery = '''update items set name = %s where id = %s'''
        cur.execute(mysqlquery, (args.get('name'), args.get('id')))
        cur.connection.commit()
    return status(True)