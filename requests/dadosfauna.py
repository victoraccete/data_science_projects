import requests as rq
import pandas as pd

jsondata = rq.get('http://api.pgi.gov.br/api/1/serie/551.json').json()
print(jsondata)
df = pd.DataFrame(jsondata)

## Tirar dúvidas para saber se o prob é a base de dados ou o código