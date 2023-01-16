from flask import current_app as app, jsonify
from flask_mysqldb import MySQL

mysql = MySQL(app)

def status(b: bool, s: str = ""):
    return dict({'status': b, 'message': s})

def select_query(query: str, values: tuple = ()):
    try:
        with mysql.connection.cursor() as cur:
            cur.execute(query, values)
            results = cur.fetchall()
            return jsonify(results)
    except Exception as e:
        return status(False, e)

def value_query(query: str, values: tuple = ()):
    try:
        with mysql.connection.cursor() as cur:
            cur.execute(query, values)
            cur.connection.commit()
        return status(True)
    except Exception as e:
        return status(False, e)