import psycopg2
import postgres_creds as creds

print("Enter New schema Name")
schema = input()

commands = ["""
    CREATE SCHEMA IF NOT EXISTS {}
            """.format(schema)]

conn = None
try:

    conn = psycopg2.connect(database=creds.DATABASE, user=creds.USER, password=creds.PASSWORD,
                            host=creds.HOST, port="5432")

    cur = conn.cursor()

    for command in commands:
        print(command)
        cur.execute(command)

    # close communication with the PostgreSQL database server
    cur.close()
    # commit the changes
    conn.commit()
except (Exception, psycopg2.DataBaseError) as error:
    print(error)

finally:
    if conn is not None:
        conn.close()
