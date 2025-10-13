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
# Store this as a dictionary called max_female_dict where the decade is the key and the category is the value. There should only be one key:value pair.

# Create a numeric female indicator (1 if Female, 0 otherwise) and compute
# the proportion of female laureates per (decade, category) by taking the mean
# of that indicator within each group.
nobel['female'] = (nobel['sex'] == 'Female').astype(int)

female_proportions = nobel.groupby(['decade', 'category'])['female'].mean()

# Find the (decade, category) with the highest female proportion
max_idx = female_proportions.idxmax()  # returns a tuple (decade, category)
max_decade, max_category = max_idx

max_female_dict = {int(max_decade): max_category}

print('decade', max_female_dict)

# Minimal assertion to ensure the result matches the expected category
assert max_female_dict[int(max_decade)] == 'Literature', (
	f"Expected category 'Literature' for decade {int(max_decade)}, got '{max_female_dict[int(max_decade)]}'"
)

# Who was the first woman to receive a Nobel Prize, and in what category?

first_woman = nobel[nobel['sex'] == 'Female']

first_woman_name = first_woman.iloc[0]['full_name']
first_woman_category = first_woman.iloc[0]['category']

print('Primera mujer nombre:', first_woman_name)
print('Primera mujer categoria:', first_woman_category)

# Which individuals or organizations have won more than one Nobel Prize throughout the years?
most_individuals = nobel['full_name'].value_counts()
most_individuals = most_individuals[most_individuals > 1]

repeat_list = list(most_individuals.index)



