from flask import current_app as app, jsonify
from flask_mysqldb import MySQL

mysql = MySQL(app)

def status(s: bool):
    return dict({'status': s})

def select_query(query: str, values: tuple = ()):
    try:
        with mysql.connection.cursor() as cur:
            cur.execute(query, values)
            results = cur.fetchall()
            return jsonify(results)
    except:
        return status(False)

def value_query(query: str, values: tuple = ()):
    try:
        with mysql.connection.cursor() as cur:
            cur.execute(query, values)
            cur.connection.commit()
        return status(True)
    except:
        return status(False)