from flask import Blueprint, request
from .utils import *

item = Blueprint('item', __name__, url_prefix='/item')


@item.route("/list-all", methods=['GET'])
def list_all():
    sql_query = '''select * from items'''
    return select_query(sql_query)


@item.route("/add", methods=['POST'])
def add_item():
    args = request.args
    sql_query = '''insert into items(name) values(%s)'''
    return value_query(sql_query, (args.get('item_name'),))


@item.route("/delete", methods=['DELETE'])
def remove_item():
    args = request.args
    sql_query = '''delete from items where id = %s'''
    return value_query(sql_query, (args.get('item_id'),))


@item.route("/update", methods=['PATCH'])
def update_item():
    args = request.args
    sql_query = '''
    update items set
    name = ifnull(%s, name)
    where id = %s
    '''
    return value_query(sql_query, (args.get('item_name'), args.get('item_id')))
