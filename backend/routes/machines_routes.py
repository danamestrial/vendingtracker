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
    return value_query(mysqlquery, (args.get("handle"), args.get("location"), args.get("status", 0)))

@machine.route("/delete-machine", methods=['DELETE'])
def delete_machine():
    args = request.args
    mysqlquery = '''delete from machines where id = %s'''
    return value_query(mysqlquery, (args.get('machine_id')))

@machine.route("/update-machine", methods=['PUT'])
def update_machine():
    args = request.args
    machine_id = args.get('machine_id')
    machine_list = select_query(f'select * from machines where id = {machine_id}')
    old_info = machine_list.get('message')[0]
    mysqlquery = '''update machines set handle = %s, location = %s, status = %s where id = %s'''
    return value_query(mysqlquery, \
        (args.get("handle", old_info.get('handle')), \
        args.get("location", old_info.get('location')), \
        args.get("status", old_info.get('status')), \
        machine_id))