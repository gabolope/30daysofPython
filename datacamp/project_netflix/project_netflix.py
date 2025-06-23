# Importing pandas and matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import os
print(os.getcwd())

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv('datacamp/project_netflix/netflix_data.csv')

######### FIRST TASK: Most frequent movie duration #########
# first: slice the movies from de 90's
movies_df = netflix_df[netflix_df['type'] == 'Movie' ] #filters only movies
min_year = movies_df[movies_df['release_year'] >= 1990 ] #filters movies after and including 1990
decade_df = min_year[min_year['release_year'] < 2000] #filter movies before 2000

# second: find the mode of the duration
#all_modes = decade_df.mode(numeric_only = True, dropna = True)
#duration = all_modes['duration']
#duration
duration_series = pd.Series(decade_df['duration']) # isolates the column duration into a one-dimensional array 
duration = int(duration_series.mode())
print(f'The most frecuent movie duration in the 90s is: {duration} minutes.')

# I made a mistake and also calculated the mean duration: 
# find the mean duration
# all_means = decade_df.mean() #returns means of all number columns
# duration = int(all_means['duration'])

# another way is to use numpy mean function: 
# duration = int(pd.mean(decade_df.loc[:, ['duration']]))

######### SECOND TASK TASK: Look for short action movies from the 90's #########
# first: slice the action movies 
action_df = decade_df[decade_df['genre'] == 'Action']

# second: slice movies shorter than 90 minutes
short_action_df = action_df[action_df['duration'] < 90]

# third: find the number of movies
short_movie_count = len(short_action_df)
print(f'The number of short action movies in the 90s is: {short_movie_count}')

plt.hist(decade_df['duration'])
plt.show()