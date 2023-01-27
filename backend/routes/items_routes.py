from flask import Blueprint, request
from .utils import *

item = Blueprint('item', __name__, url_prefix='/item')


@item.route("/list-all", methods=['GET'])
def list_all():
    mysqlquery = '''select * from items'''
    return select_query(mysqlquery)


@item.route("/add", methods=['POST'])
def add_item():
    args = request.args
    mysqlquery = '''insert into items(name) values(%s)'''
    return value_query(mysqlquery, (args.get('item_name'),))


@item.route("/delete", methods=['DELETE'])
def remove_item():
    args = request.args
    mysqlquery = '''delete from items where id = %s'''
    return value_query(mysqlquery, (args.get('item_id')))


@item.route("/update", methods=['PATCH'])
def update_item():
    args = request.args
    mysqlquery = '''
    update items set
    name = ifnull(%s, name)
    where id = %s
    '''
    return value_query(mysqlquery, (args.get('item_name'), args.get('item_id')))
