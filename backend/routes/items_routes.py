from flask import Blueprint, jsonify, request
from .utils import *

item = Blueprint('item', __name__)

@item.route("/list-all-items", methods=['GET'])
def list_all():
    mysqlquery = '''select * from items'''
    return select_query(mysqlquery)

@item.route("/add-item", methods=['POST'])
def add_item():
    args = request.args
    mysqlquery = '''insert into items(name) values(%s)'''
    return value_query(mysqlquery, (args.get('name'),))

@item.route("/remove-item", methods=['POST'])
def remove_item():
    args = request.args
    mysqlquery = '''delete from items where id = %s'''
    return value_query(mysqlquery, (args.get('id')))

@item.route("/update-item", methods=['POST'])
def update_item():
    args = request.args
    mysqlquery = '''update items set name = %s where id = %s'''
    return value_query(mysqlquery, (args.get('name'), args.get('id')))