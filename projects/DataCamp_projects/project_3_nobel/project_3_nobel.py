import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns

nobel = pd.read_csv('projects/DataCamp_projects/project_3_nobel/nobel.csv')
print(nobel.columns)

# What is the most commonly awarded gender and birth country?
top_gender = nobel['sex'].value_counts().index[0]
print('Género:', top_gender)

top_country = nobel['birth_country'].value_counts().index[0]
print('País:', top_country)

# Which decade had the highest ratio of US-born Nobel Prize winners to total winners in all categories?

# creo una columna llamada 'decade'
nobel['decade'] = (np.floor(nobel['year'] / 10) * 10).astype(int)

# junto todos los nobels de usa
usa_nobel = nobel[nobel['birth_country'] == 'United States of America']

# cuento para cada decada
usa_decades = usa_nobel['decade'].value_counts(sort=False)
total_decades = nobel['decade'].value_counts(sort=False)

# hago el ratio entre USA y totales
decade_ratio = usa_decades / total_decades

# ordeno los valores
decade_ratio = decade_ratio.sort_values(ascending=False)

max_decade_usa = decade_ratio.index[0]

print('Década de USA:', max_decade_usa)


# Which decade and Nobel Prize category combination had the highest proportion of female laureates?

# hago un index doble: por década y por categoria
nobel_indexed = nobel.set_index(['decade', 'category'])

total_laureates_index = nobel_indexed.index.value_counts(sort=False)

print(nobel_indexed['sex'].value_counts())
