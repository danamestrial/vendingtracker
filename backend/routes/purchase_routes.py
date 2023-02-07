from typing import Dict, Union

from flask import Blueprint, request

from .utils import select_query, value_query

purchase = Blueprint("purchase", __name__)

@purchase.route("/item/records", methods=["GET"])
def get_product_time_stamp():
    product_id = request.args.get("product_id")
    query = """ SELECT * FROM purchase WHERE item_id = %s"""
    return select_query(query, ((product_id),))



@purchase.route("/machine/records", methods=["GET"])
def get_machine_time_stamp():
    machine_id = request.args.get("machine_id")
    query = """ SELECT * FROM purchase WHERE machine_id = %s"""
    return select_query(query, ((machine_id),))

