import psycopg2
from config import config


def insert_tester():
    sql = '''   INSERT INTO testusers(test_name, test_surname)
                VALUES ('finally', 'finallywork') RETURNING test_id;
        '''   
    conn = None
    test_id = None
    
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql)
        # get the generated id back
        test_id = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return test_id


if __name__ == '__main__':
    insert_tester()