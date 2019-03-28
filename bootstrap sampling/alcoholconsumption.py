# -*- coding: utf-8 -*-
import pandas as pd

mat = pd.read_csv('data_science_projects/bootstrap sampling/student-mat.csv')
#por = pd.read_csv('data_science_projects/bootstrap sampling/student-por.csv')
mat = mat.drop(columns=['school', 'address', 'reason', 'nursery', 'famsize', 
                        'Pstatus', 'Mjob', 'Fjob', 'traveltime', 'schoolsup',
                        'famsup', 'guardian', 'paid', 'activities', 'higher',
                        'internet', 'romantic', 'famrel', 'freetime', 'goout',
                        'health'])

bs_sample = pd.DataFrame()
N = 1000 # tamanho da minha amostra bs
for i in range(0, N):
    bs_sample = bs_sample.append(mat.sample(replace=True))

#mat.describe()
#bs_sample.describe()
mat.mean()
bs_sample.mean()