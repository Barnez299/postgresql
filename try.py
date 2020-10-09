import psycopg2
from config import config





def get_vendors():
    """ query data from the vendors table """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("SELECT * FROM testusers ORDER BY test_name")
        row = cur.fetchall()

        
        print(row)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

   


if __name__ == '__main__':
    get_vendors()