import psycopg2
import postgres_creds as creds

conn = psycopg2.connect(database=creds.DATABASE, user=creds.USER, password=creds.PASSWORD,
                        host=creds.HOST, port="5432")

print("Connection Successful to PostgreSQL")

conn.close()
print('Connection closed')


