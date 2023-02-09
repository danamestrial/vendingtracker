from typing import Dict, Union

from flask import Blueprint, request

from .utils import select_query, snapshot, value_query

stock = Blueprint("stock", __name__, url_prefix="/stock")


@stock.route("/list", methods=["GET"])
def list_all_stocks() -> Dict[str, Union[str, list, bool]]:
    """Endpoint method to list stocks."""
    sql_query = """
    select item_id, name as "item_name", quantity
    from stocks, items
    where item_id = items.id AND machine_id = %s"""
    return select_query(sql_query, (request.args.get("machine_id"),))


@stock.route("/add", methods=["POST"])
def add_stock() -> Dict[str, Union[str, list, bool]]:
    """Endpoint method to add new stocks into machine."""
    args = request.args
    sql_query = (
        """insert into stocks(machine_id, item_id, quantity) values(%s, %s, %s)"""
    )
    return value_query(
        sql_query, (args.get("machine_id"), args.get("item_id"), args.get("quantity"))
    )


@stock.route("/delete", methods=["DELETE"])
def remove_stock() -> Dict[str, Union[str, list, bool]]:
    """Endpoint method to delete existing stock."""
    args = request.args
    sql_query = """delete from stocks where machine_id = %s and item_id = %s"""
    return value_query(sql_query, (args.get("machine_id"), args.get("item_id")))


@stock.route("/update", methods=["PATCH"])
def update_stock() -> Dict[str, Union[str, list, bool]]:
    """Endpoint method to update existing stock."""
    args = request.args
    sql_query = """
    update stocks set
    quantity = ifnull(%s, quantity)
    where machine_id = %s and item_id = %s"""

    snapshot(args.get("machine_id"), args.get("item_id"), args.get("quantity"))
    return value_query(
        sql_query, (args.get("quantity"), args.get("machine_id"), args.get("item_id"))
    )
