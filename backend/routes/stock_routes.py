from flask import Blueprint, request
from .utils import *

stock = Blueprint('stock', __name__)

@stock.route("/list-stock", methods=['POST'])
def list_all_stocks():
    mysqlquery = '''
    select item_id, name as "item_name", quantity
    from stocks, items
    where item_id = items.id AND machine_id = %s'''
    return select_query(mysqlquery, (request.args.get('machine_id')))

@stock.route("/add-stock", methods=['POST'])
def add_stock():
    args = request.args
    mysqlquery = '''insert into stocks(machine_id, item_id, quantity) values(%s, %s, %s)'''
    return value_query(mysqlquery, (args.get('machine_id'), args.get('item_id'), args.get('quantity')))

@stock.route("/remove-stock", methods=['POST'])
def remove_stock():
    args = request.args
    mysqlquery = '''delete from stocks where machine_id = %s and item_id = %s'''
    return value_query(mysqlquery, (args.get('machine_id'), args.get('item_id')))

@stock.route("/update-stock", methods=['POST'])
def update_stock():
    args = request.args
    mysqlquery = '''update stocks set quantity = %s where machine_id = %s and item_id = %s'''
    return value_query(mysqlquery, (args.get('quantity'), args.get('machine_id'), args.get('item_id')))