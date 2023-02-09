from typing import Dict, Union

from flask import Blueprint, request

from .utils import select_query, value_query

item = Blueprint("item", __name__, url_prefix="/item")


@item.route("/list-all", methods=["GET"])
def list_all() -> Dict[str, Union[str, list, bool]]:
    """Endpoint method to list out items."""
    sql_query = """select * from items"""
    return select_query(sql_query)


@item.route("/add", methods=["POST"])
def add_item() -> Dict[str, Union[str, list, bool]]:
    """Endpoint method to add new item."""
    args = request.args
    sql_query = """insert into items(name) values(%s)"""
    return value_query(sql_query, (args.get("item_name"),))


@item.route("/delete", methods=["DELETE"])
def remove_item() -> Dict[str, Union[str, list, bool]]:
    """Endpoint method to delete existing item."""
    args = request.args
    sql_query = """delete from items where id = %s"""
    return value_query(sql_query, (args.get("item_id"),))


@item.route("/update", methods=["PATCH"])
def update_item() -> Dict[str, Union[str, list, bool]]:
    """Endpoint method to update existing item."""
    args = request.args
    sql_query = """
    update items set
    name = ifnull(%s, name)
    where id = %s
    """
    return value_query(sql_query, (args.get("item_name"), args.get("item_id")))


@item.route("/records", methods=["GET"])
def get_product_time_stamp() -> Dict[str, Union[str, list, bool]]:
    """Endpoint to get logs of changes to items."""
    product_id = request.args.get("product_id")
    query = """ SELECT * FROM purchase WHERE item_id = %s"""
    return select_query(query, (product_id,))
