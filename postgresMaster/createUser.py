import psycopg2
import postgres_creds as creds


# for general write access
# access = SELECT, UPDATE, INSERT, DELETE

# for general select access
# access = SELECT

print("Enter New ROLE Name")
role = input()

print("Enter SCHEMA NAME Access")
schema = input()

print("Enter ACCESS TYPE")
access = input()

print("Enter NEW USER NAME")
name = input()

print("Enter USER PASSWORD")
pw = input()

# commands needed to set up user and access
commands = [
"""
    CREATE ROLE {}
            """.format(role),
"""
    GRANT USAGE ON SCHEMA {} TO {}
            """.format(schema, role),
"""
    GRANT {} ON ALL TABLES IN SCHEMA {} TO {}
            """.format(access, schema, role),
"""
    ALTER DEFAULT PRIVILEGES IN SCHEMA {} GRANT {} ON TABLES TO {}
            """.format(schema, access, role),
"""
    CREATE USER {} WITH PASSWORD {}
            """.format(name, pw),
"""
    GRANT {} TO {}
            """.format(role, name)
            ]

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


