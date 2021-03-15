import pandas as pd
from sqlalchemy import create_engine
import pymysql


def db_init():
    conn = pymysql.connect(host='127.0.0.1', user='test', password='test', database='testdb')
    cursor = conn.cursor()
    return conn

def create_table(conn):
    sql = """CREATE TABLE IF NOT EXISTS test_tb(id integer PRIMARY KEY, name text);"""
    try:
        c = conn.cursor()
        c.execute(sql)
        sql_print(sql)
    except Exception as e:
        print(e)

def insert_one_row(conn, insert_vals):
    print(type((insert_vals)))
    # sql = """INSERT INTO test_tb(id, name) VALUES(?,?)""" # ERROR
    sql = """INSERT INTO test_tb(id, name) VALUES(%s,%s)"""
    cur = conn.cursor()
    cur.execute(sql, insert_vals)
    conn.commit()
    sql_print(sql)
    return cur.lastrowid

def select_all_rows(conn):
    sql = """SELECT * from test_tb"""
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()

    for row in rows:
        print(row)
    sql_print(sql)

def delete_all_rows(conn):
    sql = """DELETE FROM test_tb"""
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    sql_print(sql)
    return conn

def drop_one_table(conn):
    sql = """DROP TABLE test_tb"""

    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    sql_print(sql)
    return conn

def update_one_row(conn, update_vals):
    sql = """UPDATE test_tb SET id = %s, name = %s WHERE id =%s"""
    cur = conn.cursor()
    cur.execute(sql, update_vals)
    conn.commit()
    sql_print(sql)
    return conn

def sql_print(sql):
    print(f"COMPLETE SQL STMT EXECUTION:: {sql}\n")


if __name__ == "__main__":
    conn = db_init()
    create_table(conn=conn)
    with conn:
        for num in range(1, 20):
            insert_vals=(num, "row num "+str(num))
            insert_one_row(conn, insert_vals)

        select_all_rows(conn)
        drop_one_table(conn)
