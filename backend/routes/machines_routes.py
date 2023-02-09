from typing import Dict, Union

from flask import Blueprint, request

from .utils import select_query, value_query

machine = Blueprint("machine", __name__, url_prefix="/machine")


@machine.route("/list-all", methods=["GET"])
def list_all() -> Dict[str, Union[str, list, bool]]:
    """Endpoint method to list all machines."""
    sql_query = """select * from machines"""
    return select_query(sql_query)


@machine.route("/add", methods=["POST"])
def add_machine() -> Dict[str, Union[str, list, bool]]:
    """Endpoint method to add new machine."""
    args = request.args
    sql_query = """insert into machines(handle, location, status) values (%s, %s, %s)"""
    return value_query(
        sql_query, (args.get("handle"), args.get("location"), args.get("status", 0))
    )


@machine.route("/delete", methods=["DELETE"])
def delete_machine() -> Dict[str, Union[str, list, bool]]:
    """Endpoint method to delete existing machine."""
    args = request.args
    sql_query = """delete from machines where id = %s"""
    return value_query(sql_query, (args.get("machine_id"),))


@machine.route("/update", methods=["PATCH"])
def update_machine() -> Dict[str, Union[str, list, bool]]:
    """Endpoint method to update existing machine."""
    args = request.args
    sql_query = """
    update machines set
    handle = ifnull(%s, handle),
    location = ifnull(%s, location),
    status = ifnull(%s, status)
    where id = %s
    """
    return value_query(
        sql_query,
        (
            args.get("handle"),
            args.get("location"),
            args.get("status"),
            args.get("machine_id"),
        ),
    )


@machine.route("/records", methods=["GET"])
def get_machine_time_stamp() -> Dict[str, Union[str, list, bool]]:
    """Endpoint to get logs of changes to machines."""
    machine_id = request.args.get("machine_id")
    query = """ SELECT * FROM purchase WHERE machine_id = %s"""
    return select_query(query, (machine_id,))
