import pandas as pd
from pandasql import sqldf as psql
import sqlite3 as lite

## USANDO UM PANDAS DF COMO UMA TABLE ##
data = {'funcionario': ['Severino', 'Benedito', 'Aparecida', 'Marlene', 'Rosa',
                        'Sebastião', 'Valentina', 'Jimi Hendrix', 'Rita'], 
     'salario': [900, 1100, 840, 1250, 980, 1400, 925, 760, 1900]}
Salaries = pd.DataFrame(data=data)

psql("SELECT * FROM Salaries").head()


## AGORA CRIANDO UMA TABELA E EXPORTANDO PARA UM PANDAS DF
con = lite.connect('test.db')
cur = con.cursor()
cur.execute("CREATE TABLE music(album TEXT, artista TEXT, lançamento TEXT)")
cur.execute("INSERT INTO music VALUES('Walls of Jericho', 'Helloween', '1985')")
cur.execute("INSERT INTO music VALUES('Visions', 'Stratovarius', '1997')")
cur.execute("INSERT INTO music VALUES('Once', 'Nightwish', '2004')")

albums_df = pd.read_sql_query("SELECT * FROM music", con)