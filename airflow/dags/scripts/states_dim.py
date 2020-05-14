import requests
import pandas as pd
import psycopg2
import postgres_creds as creds

print(creds.DATABASE)

"""
Called daily to replace covid_tracking.states -- Dimensional Table
"""


states_dim = pd.DataFrame(requests.get("https://covidtracking.com/api/v1/states/info.json").json())
print(states_dim.head())

states_dim_trim = states_dim[['state', 'name']]
# states_dim.to_sql('covidtracking.states', postgresCon, if_exists='replace')
print(states_dim_trim.head())

# conn = None
# try:
#
#     conn = psycopg2.connect(database=creds.DATABASE, user=creds.USER, password=creds.PASSWORD,
#                             host=creds.HOST, port="5432")
#
#     cur = conn.cursor()
#
#     for command in commands:
#         print(command)
#         cur.execute(command)
#
#     # close communication with the PostgreSQL database server
#     cur.close()
#     # commit the changes
#     conn.commit()
# except (Exception, psycopg2.DataBaseError) as error:
#     print(error)
#
# finally:
#     if conn is not None:
#         conn.close()
