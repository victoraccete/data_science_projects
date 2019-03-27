# -*- coding: utf-8 -*-
import pandas as pd

mat = pd.read_csv('data_science_projects/bootstrap sampling/student-mat.csv')
#por = pd.read_csv('data_science_projects/bootstrap sampling/student-por.csv')

mat = mat.drop(columns=['school', 'address', 'reason', 'nursery', 'famsize', 
                        'Pstatus', 'Mjob', 'Fjob', 'traveltime', 'schoolsup',
                        'famsup'])
