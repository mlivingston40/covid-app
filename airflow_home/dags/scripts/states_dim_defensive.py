import psycopg2
import postgres_creds as creds

"""
Called before states_dim.py as defensive programming to drop all rows
"""

conn = None
try:

    conn = psycopg2.connect(database=creds.DATABASE, user=creds.USER, password=creds.PASSWORD,
                            host=creds.HOST, port="5432")

    cur = conn.cursor()

    command = """DELETE FROM covid_tracking.states"""

    cur.execute(command)

    # commit the changes
    conn.commit()

    # close communication with the PostgreSQL database server
    cur.close()

except (Exception, psycopg2.DataBaseError) as error:
    print(error)

finally:
    if conn is not None:
        conn.close()
