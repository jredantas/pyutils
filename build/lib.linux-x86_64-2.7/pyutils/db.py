'''
Created on Jun 7, 2017

@author: 09959295800

Some utilities for database manipulation.
'''

import psycopg2 

def open_database(dbname='radar', user='icvisual2', host='10.139.6.31'):
    connStr = "dbname='%s' user='%s' host='%s'" % (dbname, user, host)
    conn = psycopg2.connect(connStr)
    return conn

def close_database(conn):
    conn.close()
