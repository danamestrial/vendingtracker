from flask import Blueprint, request
from .utils import *

machine = Blueprint('machine', __name__, url_prefix='/machine')


@machine.route('/list-all', methods=['GET'])
def list_all():
    mysqlquery = '''select * from machines'''
    return select_query(mysqlquery)


@machine.route('/add', methods=['POST'])
def add_machine():
    args = request.args
    mysqlquery = '''insert into machines(handle, location, status) values (%s, %s, %s)'''
    return value_query(mysqlquery, (args.get("handle"), args.get("location"), args.get("status", 0)))


@machine.route("/delete", methods=['DELETE'])
def delete_machine():
    args = request.args
    mysqlquery = '''delete from machines where id = %s'''
    return value_query(mysqlquery, (args.get('machine_id'),))


@machine.route("/update", methods=['PATCH'])
def update_machine():
    args = request.args
    mysqlquery = '''
    update machines set
    handle = ifnull(%s, handle),
    location = ifnull(%s, location),
    status = ifnull(%s, status)
    where id = %s
    '''
    return value_query(mysqlquery, \
                       (args.get("handle"), \
                        args.get("location"), \
                        args.get("status"), \
                        args.get("machine_id")))
