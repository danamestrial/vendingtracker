from flask import Blueprint, jsonify, request
from .utils import *

stock = Blueprint('stock', __name__)

@stock.route("/list-stocks", methods=['POST'])
def list_all_stocks():
    mysqlquery = '''
    select item_id, name as "item_name", quantity
    from stocks, items
    where item_id = items.id AND machine_id = %s'''
    return select_query(mysqlquery, request.args.get('id'))