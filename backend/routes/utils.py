from flask import current_app as app, session, redirect
from flask_mysqldb import MySQL

mysql = MySQL(app)

def status(s: bool):
    return dict({'status': s})