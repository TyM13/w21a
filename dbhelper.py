import mariadb
import dbcreds

def connect_db():
    try:
        conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password,
        host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor = conn.cursor()
        return cursor
    except mariadb.OperationalError as error:
        print("operational error", error)
    except Exception as error:
        print("unknown error", error)

def close_connect(cursor):
    try:
        conn = cursor.connection
        cursor.close()
        conn.close()
    except mariadb.OperationalError as error:
        print('operational error', error)
    except mariadb.InternalError as error:
        print('internal error', error)
    except Exception as error:
        print('unknown error', error)


def execute_statment(cursor, statement, list_of_args=[]): 
    try:
        cursor.execute(statement, list_of_args)
        results = cursor.fetchall()
        return results
    except mariadb.ProgrammingError as error:
        print('programming error', error)
        return str(error)
    except mariadb.IntegrityError as error:
        print('integrity error', error)
        return str(error)
    except mariadb.DataError as error:
        print('data error', error)
        return str(error)
    except Exception as error:
        print('unknown error', error)
        return str(error)

def run_statment(statment, list_of_args=[]):
    cursor = connect_db()
    if(cursor == None):
        return "conntection error"
    results = execute_statment(cursor, statment, list_of_args)
    close_connect(cursor)
    return results