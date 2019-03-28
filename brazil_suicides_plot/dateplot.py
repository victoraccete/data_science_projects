# -*- coding: utf-8 -*-
import pandas as pd
suicide_rates = pd.read_csv('data_science_projects/brazil_suicides_plot/master.csv')
br_rates = suicide_rates[suicide_rates['country']=='Brazil'][suicide_rates['sex'] 
                        == 'male'][suicide_rates['age']=='15-24 years']

br_rates.year = pd.to_datetime(br_rates.year, format='%Y')
br_rates.plot(x='year', y='suicides/100k pop')