from flask import Blueprint, request
from .utils import *

machine = Blueprint('machine', __name__)

@machine.route('/list-all-machines', methods=['GET'])
def list_all():
    mysqlquery = '''select * from machines'''
    return select_query(mysqlquery)

@machine.route('/add-machine', methods=['POST'])
def add_machine():
    args = request.args
    mysqlquery = '''insert into machines(handle, location, status) values (%s, %s, %s)'''
    return value_query(mysqlquery, (args.get("handle"), args.get("location"), args.get("status")))

@machine.route("/delete-machine", methods=['POST'])
def delete_machine():
    args = request.args
    mysqlquery = '''delete from machines where id = %s'''
    return value_query(mysqlquery, (args.get('id')))

@machine.route("/update-machine", methods=['POST'])
def update_machine():
    args = request.args
    mysqlquery = '''update machines set handle = %s, location = %s, status = %s where id = %s'''
    return value_query(mysqlquery, (args.get("handle"), args.get("location"), args.get("status"), args.get("id")))