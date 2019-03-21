import requests as rq
import pandas as pd

## Dados sobre quedas de meteoritos ##
jsondata = rq.get('https://data.nasa.gov/resource/y77d-th95.json').json()
print(jsondata)
df = pd.DataFrame(jsondata)

df.mass[1]
df.mass = pd.to_numeric(df.mass)
df.mass[1]

type(df.mass[0])