import requests
import pandas as pd
import psycopg2
import postgres_creds as creds

"""
Called daily to replace covid_tracking.states -- Dimensional Table
"""

states_dim = pd.DataFrame(requests.get("https://covidtracking.com/api/v1/states/info.json").json())

states_dim_trim = states_dim[['state', 'name']]

combinedTupleList = [[s, n] for s, n in zip(states_dim_trim.state, states_dim_trim.name)]
print(combinedTupleList)

conn = None
try:

    conn = psycopg2.connect(database=creds.DATABASE, user=creds.USER, password=creds.PASSWORD,
                            host=creds.HOST, port="5432")

    cur = conn.cursor()

    command = """INSERT INTO covid_tracking.states (state, name) VALUES(%s, %s)"""

    cur.executemany(command, combinedTupleList)

    # commit the changes
    conn.commit()

    # close communication with the PostgreSQL database server
    cur.close()

except (Exception, psycopg2.DataBaseError) as error:
    print(error)

finally:
    if conn is not None:
        conn.close()
