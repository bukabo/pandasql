from pandasql import sqldf
import pandas as pd
import numpy as np

users_id = np.arange(1, 1000)
prod_id = np.arange(1, 100)

action = ['камень', 'ножницы', 'бумага']
act = np.random.choice(action, 999)

start_date = pd.to_datetime('2022-01-01')
times = pd.date_range(start_date, periods=999, freq='D')

df = pd.DataFrame({'id': users_id,
                   'date': times})
df['action'] = act
df['action2'] = np.random.choice(action, len(df))

# print(df.groupby(['action']).size())

sql = """Select action, action2, count(*) as cnt from df 
      --where action = 'камень'
      group by action, action2
      """

print(sqldf(sql))
