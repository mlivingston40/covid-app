import requests
import pandas as pd
from sqlalchemy import create_engine


# should figure out best way to export evn connection of postgres for all of airflow app
# UN = ''
# PW = ''
# EP = ''
# DB = ''
# PORT = ''
# cxn_string = 'postgresql://'+UN+':'+PW+'@'+EP+':'+PORT+'/'+DB
# postgresCon = create_engine(cxn_string)


# https://covidtracking.com/api/v1/states/info.json

states_dim = pd.DataFrame(requests.get("https://covidtracking.com/api/v1/states/info.json").json())
print(states_dim.head())

# states_dim.to_sql('covidtracking.states', postgresCon, if_exists='replace')