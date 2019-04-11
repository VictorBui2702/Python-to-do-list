# db_utils.py
import os  
import sqlite3
import fire

# create a default path to connect to and create (if necessary) a database
# called 'database.sqlite3' in the same directory as this script
DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'database.sqlite3')
print(DEFAULT_PATH)


def db_connect(db_path=DEFAULT_PATH):  
    con = sqlite3.connect(db_path)
    return con

def db_create():
    con = db_connect()
    sql = """
       CREATE TABLE IF NOT EXISTS todos (
           id INTEGER PRIMARY KEY, 
           todo_text text NOT NULL
       )  
    """
    cur = con.cursor()
    cur.execute(sql)
    con.close()

def add_todo(todo_text):
    con = db_connect()
    sql = """
        INSERT INTO todos (todo_text)
        VALUES (?)
    """
    cur = con.cursor()
    cur.execute(sql, (todo_text,) )
    con.commit() 

    select_sql = """
        SELECT * from todos;
    """
    cur.execute(select_sql) 
    results = cur.fetchall()
    for row in results:
        print(row)

    con.close()


def del_todo():
    con = db_connect()
    del_sql = """
        DELETE FROM todos WHERE id = (?);
    """
    cur = con.cursor()
    cur.execute(del_sql, (3,)) 
    # results = cur.fetchall()
    # for row in results:
    #     print(row)
    con.commit() 
    
    select_sql = """
        SELECT * from todos;
    """
    cur.execute(select_sql) 
    results = cur.fetchall()
    for row in results:
        print(row)
    
    con.close()


db_create()

if __name__ == '__main__':
    # fire.Fire({
    #     'add_todo': add_todo
    # })
    fire.Fire()



