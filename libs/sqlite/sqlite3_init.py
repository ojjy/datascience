import sqlite3


def init_connection(dbf):
    try:
        conn = sqlite3.connect(dbf)
        return conn
    except Exception as e:
        print(e)
    return conn

def create_table(conn, create_tb):
    try:
        c = conn.cursor()
        c.execute(create_tb)
        print("success to create table")
    except Exception as e:
        print(e)



def insert_one_row(conn, insert_vals):
    sql = ''' INSERT INTO test_tb(id, name)
                  VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, insert_vals)
    conn.commit()

    return cur.lastrowid

if __name__ == "__main__":
    dbf = "test.db"
    create_tb = """
    CREATE TABLE IF NOT EXISTS test_tb(
    id integer PRIMARY KEY,
    name text
    );
    """
    conn = init_connection(dbf)

    if conn is not None:
        create_table(conn=conn, create_tb=create_tb)
    else:
        print("Error")

    with conn:
        insert_vals = (1, "row num 1")
        insert_one_row(conn, insert_vals)
