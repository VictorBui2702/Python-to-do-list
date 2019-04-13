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

#create todo list
def db_create():
    con = db_connect()
    sql = """
       CREATE TABLE IF NOT EXISTS todos (
           id INTEGER PRIMARY KEY, 
           tasks text NOT NULL,
           due_date DATETIME,
           status TEXT DEFAULT "incomplete"
       )  
    """
    cur = con.cursor()
    cur.execute(sql)
    con.close()

def add_todo(todo_text):
    con = db_connect()
    sql = """
        INSERT INTO todos (tasks)
        VALUES (?)
    """
    cur = con.cursor()
    cur.execute(sql, (todo_text,) )
    con.commit() 


    select_sql = """
        SELECT * from todos
    """
    cur.execute(select_sql) 
    results = cur.fetchall()
    print(results[-1])

    con.close()


def add_due_date(due_date, id):
    con = db_connect()
    
    sql = """
        UPDATE todos
        SET due_date = (?)
        WHERE id = (?)
    """

    value = (due_date, id,)

    cur = con.cursor()
    cur.execute(sql, value )
    con.commit() 

    select_sql = """
        SELECT * from todos
    """
    cur.execute(select_sql) 
    results = cur.fetchall()
    for row in results:
        print(row)

    con.close()

def update_project_id(project_id, id):
    con = db_connect()
    
    sql = """
        UPDATE todos
        SET project_id = (?)
        WHERE id = (?)
    """

    value = (project_id, id,)

    cur = con.cursor()
    cur.execute(sql, value )
    con.commit() 

    select_sql = """
        SELECT * from todos
    """
    cur.execute(select_sql) 
    results = cur.fetchall()
    for row in results:
        print(row)

    con.close()


def del_todo(id):
    con = db_connect()
    del_sql = """
        DELETE FROM todos WHERE id = (?)
    """
    cur = con.cursor()
    cur.execute(del_sql, (id,) )
    con.commit() 
    
    select_sql = """
        SELECT * from todos
    """
    cur.execute(select_sql) 
    results = cur.fetchall()
    for row in results:
        print(row)
    
    con.close()


def mark_complete(id):
    con = db_connect()
    sql = """
        UPDATE todos
        SET status = CASE status
                     WHEN 'incomplete' THEN 'complete'
                     ELSE   'incomplete'
                     END
        WHERE id = ?
    """
    value = (id,)
    cur = con.cursor()
    cur.execute(sql, value )
    con.commit() 

    select_sql = """
        SELECT * from todos;
    """
    cur.execute(select_sql) 
    results = cur.fetchall()
    for row in results:
        print(row)

    con.close()

def list_tasks(status="", project_id="", due_date_order=""):
    con = db_connect() 
    cur = con.cursor()

    # list sorted by status
    if  project_id == "" and due_date_order == "":
        select_sql = """
            SELECT * from todos
            WHERE status = (?)
        """
        cur.execute(select_sql, (status,)) 

    # list sorted by project_id
    elif  status == "" and due_date_order == "":
        select_sql = """
            SELECT * from todos
            WHERE project_id = (?)
        """
        cur.execute(select_sql, (project_id,)) 

    # list by due date ASC
    elif  status == "" and project_id == "":
        select_sql = """
            SELECT * from todos
            ORDER BY due_date ASC 
        """
        cur.execute(select_sql, (due_date_order,)) 

    # list by due date DESC
    elif  status == "" and project_id == "":
        select_sql = """
            SELECT * from todos
            ORDER BY due_date ASC 
        """
        cur.execute(select_sql, (due_date_order,)) 

    # list sorted by status and project_id
    elif  due_date_order == "":
        select_sql = """
            SELECT * from todos
            WHERE status = (?) AND project_id = (?)
        """
        value = (status,project_id)
        cur.execute(select_sql, value )  

    results = cur.fetchall()
    for row in results:
        print(row)
    con.commit() 
    con.close()


def add_column():
    con = db_connect()
    
    sql = """
        ALTER TABLE todos
        ADD COLUMN project_id TEXT
    """
    # value = (column_name, datatype)
    cur = con.cursor()
    cur.execute(sql,)
    con.commit() 

    select_sql = """
        SELECT * from todos
    """
    cur.execute(select_sql) 
    results = cur.fetchall()
    for row in results:
        print(row)

    con.close()

# This function drop_column below is not working for SQLite?!
def drop_column():
    con = db_connect()
    
    sql = """
        ALTER TABLE todos
        DROP COLUMN student
    """
    # value = (column_name,)
    cur = con.cursor()
    cur.execute(sql,)
    con.commit() 

    select_sql = """
        SELECT * from todos
    """
    cur.execute(select_sql) 
    results = cur.fetchall()
    for row in results:
        print(row)

    con.close()

db_create()

#create project list
def db_create_project():
    con = db_connect()
    sql = """
       CREATE TABLE IF NOT EXISTS projects (
           id INTEGER PRIMARY KEY, 
           projects TEXT NOT NULL,
           due_date DATETIME,
           status TEXT DEFAULT "incomplete"
       )  
    """
    cur = con.cursor()
    cur.execute(sql)
    con.close()

def add_project(id, projects, due_date):
    con = db_connect()
    sql = """
        INSERT INTO projects (id, projects, due_date)  
        VALUES (?,?,?)
    """
    cur = con.cursor()
    cur.execute(sql, (id, projects, due_date) )
    con.commit() 

    select_sql = """
        SELECT * from projects
    """
    cur.execute(select_sql) 
    results = cur.fetchall()
    print(results[-1])

    con.close()

db_create_project()

# Update due date of the project
def update_project_due_date(due_date, id):
    con = db_connect()
    
    sql = """
        UPDATE projects
        SET due_date= (?)
        WHERE id = (?)
    """

    value = (due_date, id,)

    cur = con.cursor()
    cur.execute(sql, value )
    con.commit() 

    select_sql = """
        SELECT * from projects
    """
    cur.execute(select_sql) 
    results = cur.fetchall()
    for row in results:
        print(row)

    con.close()

# Update name of the project
def update_project_name(projects, id):
    con = db_connect()
    
    sql = """
        UPDATE projects
        SET projects= (?)
        WHERE id = (?)
    """

    value = (projects, id,)

    cur = con.cursor()
    cur.execute(sql, value )
    con.commit() 

    select_sql = """
        SELECT * from projects
    """
    cur.execute(select_sql) 
    results = cur.fetchall()
    for row in results:
        print(row)

    con.close()

if __name__ == '__main__':
    # fire.Fire({
    #     'add_todo': add_todo
    # })
    fire.Fire()



