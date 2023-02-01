from flask import Blueprint, request

from .utils import *

machine = Blueprint('machine', __name__, url_prefix='/machine')


@machine.route('/list-all', methods=['GET'])
def list_all():
    sql_query = '''select * from machines'''
    return select_query(sql_query)


@machine.route('/add', methods=['POST'])
def add_machine():
    args = request.args
    sql_query = '''insert into machines(handle, location, status) values (%s, %s, %s)'''
    return value_query(sql_query, (args.get("handle"), args.get("location"), args.get("status", 0)))


@machine.route("/delete", methods=['DELETE'])
def delete_machine():
    args = request.args
    sql_query = '''delete from machines where id = %s'''
    return value_query(sql_query, (args.get('machine_id'),))


@machine.route("/update", methods=['PATCH'])
def update_machine():
    args = request.args
    sql_query = '''
    update machines set
    handle = ifnull(%s, handle),
    location = ifnull(%s, location),
    status = ifnull(%s, status)
    where id = %s
    '''
    return value_query(sql_query, \
                       (args.get("handle"), \
                        args.get("location"), \
                        args.get("status"), \
                        args.get("machine_id")))
