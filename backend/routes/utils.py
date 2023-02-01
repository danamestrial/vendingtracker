from pymysql.cursors import DictCursor

from app import mysql


def status(b: bool, s: str = ""):
    return dict({'status': b, 'message': s})


def select_query(query: str, values: tuple = (), mysql_instance=mysql):
    try:
        with mysql_instance.get_db().cursor(DictCursor) as cur:
            cur.execute(query, values)
            results = cur.fetchall()
            return status(True, results)
    except Exception as e:
        return status(False, str(e))


def value_query(query: str, values: tuple = (), mysql_instance=mysql):
    try:
        with mysql_instance.get_db().cursor(DictCursor) as cur:
            cur.execute(query, values)
            cur.connection.commit()
        return status(True)
    except Exception as e:
        return status(False, str(e))
