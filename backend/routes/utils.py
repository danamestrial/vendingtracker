from typing import Dict, Union

from app import mysql
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor


def status(b: bool, s: Union[str, list] = "") -> Dict[str, Union[str, list, bool]]:
    """To get a constant responses every query."""
    return dict({"status": b, "message": s})


def select_query(
    query: str, values: tuple = (), mysql_instance: MySQL = mysql
) -> status:
    """To execute mysql query for select command."""
    try:
        with mysql_instance.get_db().cursor(DictCursor) as cur:
            cur.execute(query, values)
            results = cur.fetchall()
            return status(True, results)
    except Exception as e:
        return status(False, str(e))


def value_query(
    query: str, values: tuple = (), mysql_instance: MySQL = mysql
) -> status:
    """To execute mysql query for command that doesn't return."""
    try:
        with mysql_instance.get_db().cursor(DictCursor) as cur:
            cur.execute(query, values)
            cur.connection.commit()
        return status(True)
    except Exception as e:
        return status(False, str(e))
