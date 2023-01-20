from flask import Blueprint, request
from .utils import *

stock = Blueprint('stock', __name__, url_prefix='/stock')

@stock.route("/list", methods=['GET'])
def list_all_stocks():
    mysqlquery = '''
    select item_id, name as "item_name", quantity
    from stocks, items
    where item_id = items.id AND machine_id = %s'''
    return select_query(mysqlquery, (request.args.get('machine_id')))

@stock.route("/add", methods=['POST'])
def add_stock():
    args = request.args
    mysqlquery = '''insert into stocks(machine_id, item_id, quantity) values(%s, %s, %s)'''
    return value_query(mysqlquery, (args.get('machine_id'), args.get('item_id'), args.get('quantity')))

@stock.route("/remove", methods=['DELETE'])
def remove_stock():
    args = request.args
    mysqlquery = '''delete from stocks where machine_id = %s and item_id = %s'''
    return value_query(mysqlquery, (args.get('machine_id'), args.get('item_id')))

@stock.route("/update", methods=['PUT'])
def update_stock():
    args = request.args
    mysqlquery = '''
    update stocks set
    quantity = ifnull(%s, quantity)
    where machine_id = %s and item_id = %s'''
    return value_query(mysqlquery, (args.get('quantity'), args.get('machine_id'), args.get('item_id')))