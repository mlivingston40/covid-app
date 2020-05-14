import psycopg2
import postgres_creds as creds

commands = [
    """
    CREATE TABLE IF NOT EXISTS covid_tracking.states (
        state VARCHAR(2) PRIMARY KEY,
        name VARCHAR(35)
    )
    """,
    """ CREATE TABLE IF NOT EXISTS covid_tracking.states_daily (
            date DATE PRIMARY KEY,
            state VARCHAR(2),
            positive INTEGER,
            negative INTEGER,
            pending INTEGER,
            recovered INTEGER,
            hospitalizedCurrently INTEGER,
            inIcuCurrently INTEGER,
            onVentilatorCurrently INTEGER,
            deathIncrease INTEGER,
            hospitalizedIncrease INTEGER,
            negativeIncrease INTEGER,
            positiveIncrease INTEGER,
            totalTestResultsIncrease INTEGER,
            dataQualityGrade VARCHAR(3),
            FOREIGN KEY (state) REFERENCES covid_tracking.states (state)
            )
    """,
    """
    CREATE TABLE IF NOT EXISTS covid_tracking.states_agg (
            state VARCHAR(2) PRIMARY KEY,
            positive INTEGER,
            negative INTEGER,
            pending INTEGER,
            recovered INTEGER,
            hospitalizedCurrently INTEGER,
            inIcuCurrently INTEGER,
            onVentilatorCurrently INTEGER,
            total INTEGER,
            totalTestResults INTEGER,
            dataQualityGrade VARCHAR(3)
    )
    """
    # """
    # CREATE TABLE IF NOT EXISTS us_daily (
    # )
    # """,
    # """
    # CREATE TABLE IF NOT EXISTS us_agg (
    # )
    # """
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
