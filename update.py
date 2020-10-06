import psycopg2
from config import config


def update_tester():
    sql = '''   UPDATE testusers
                    SET test_surname = 'updatesurname'
                    WHERE test_id = 9
        '''   
    conn = None
    
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
        # test_id = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    update_tester()