# dataexer.py
# https://jsonplaceholder.typicode.com/todos

import requests
import json
import pandas as pd
import numpy as np

def p(data):
    print(data, '\n')

# 1
response = requests.get('https://jsonplaceholder.typicode.com/todos')
data = response.json()
print(data)

df = pd.DataFrame(data)
print(df)

resultdf = df.assign(result = np.where(df['userId']>=5,"pass",'fail'))
print(resultdf)

# 2
result = resultdf.query("userId>=5")[['userId', 'id', 'title', 'completed']]
print(result)

# 3
result = result.sort_values("userId", ascending=False)
print(result)

# 4
result.to_csv('result.csv', index = False)
result.to_json('result.json', indent = 4)
result.to_xml('result.xml', index = False)




