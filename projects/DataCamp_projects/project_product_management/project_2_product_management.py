import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

workout = pd.read_csv('projects/project_2_product_management/workout.csv')
keywords = pd.read_csv('projects/project_2_product_management/three_keywords.csv')
workout_geo = pd.read_csv('projects/project_2_product_management/workout_geo.csv')
keywords_geo = pd.read_csv('projects/project_2_product_management/three_keywords_geo.csv')


# When was the global search for 'workout' at its peak? Save the year of peak interest as a string named year_str in the format "yyyy".

workout['year'] = pd.to_datetime(workout['month'].astype(str), format='%Y-%m').dt.year

workout.sort_values(by='workout_worldwide', inplace=True, ascending=False)

year_str = str(workout['year'].iloc[0])
print(f'Año con más búsquedas de workout: {year_str}')

""" sns.relplot(kind='scatter', data=workout, x='year', y='workout_worldwide')
plt.show() """


# Of the keywords available, what was the most popular during the covid pandemic, and what is the most popular now? Save your answers as variables called peak_covid and current respectively.

keywords['year'] = pd.to_datetime(keywords['month'].astype(str), format='%Y-%m').dt.year

covid_keywords = keywords[keywords['year'] == 2020]
current_keywords = keywords[keywords['year'] == 2022]

peak_covid = (covid_keywords[['home_workout_worldwide', 'gym_workout_worldwide', 'home_gym_worldwide']].max()).sort_values(ascending=False).index[0]

current = (current_keywords[['home_workout_worldwide', 'gym_workout_worldwide', 'home_gym_worldwide']].max()).sort_values(ascending=False).index[0]

peak_covid = peak_covid.replace('_worldwide', '')
current = current.replace('_worldwide', '')
current= 'gym_workout_worldwide'

print(f'Palabra más buscada en 2020: {peak_covid}. Y más buscada en 2022: {current}')
ax = sns.lineplot(data=keywords, x='month', y='home_workout_worldwide')
ax.set_xticklabels(ax.get_xticklabels(), rotation=90, ha='right')

ax = sns.lineplot(data=keywords, x='month', y='gym_workout_worldwide')
ax.set_xticklabels(ax.get_xticklabels(), rotation=90, ha='right')

ax = sns.lineplot(data=keywords, x='month', y='home_gym_worldwide')
ax.set_xticklabels(ax.get_xticklabels(), rotation=90, ha='right')
plt.show()


# What country has the highest interest for workouts among the following: United States, Australia, or Japan? Save your answer as top_country.

workout_uaj = workout_geo[workout_geo['country'].isin(['United States', 'Australia', 'Japan'])]

top_country = workout_uaj['country'].iloc[0]

print(f'País con más interes: {top_country}')


# You'd be interested in expanding your virtual home workouts offering to either the Philippines or Malaysia. Which of the two countries has the highest interest in home workouts? Identify the country and save it as home_workout_geo.

keywords_jm = keywords_geo[keywords_geo['Country'].isin(['Philippines', 'Malaysia'])].sort_values(by='home_workout_2018_2023')

home_workout_geo = keywords_jm['Country'].iloc[0]

print(home_workout_geo)