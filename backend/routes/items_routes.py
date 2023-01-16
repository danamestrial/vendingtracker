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

# @item.route("/add_item", methods=['POST'])
# def add_item():
#     with mysql.connection.cursor() as cur:
