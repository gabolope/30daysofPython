import numpy as np
import pandas as pd

# 1 Read the hacker_news.csv file from data directory
df = pd.read_csv('./day_25_pandas/hacker_news.csv')

# 2 Get the first five rows
print(df.head)

# 3 Get the last five rows
print(df.tail)

# 4 Get the title column as pandas series
titles = df['title']

print('\n ##################')
print(titles)

# 5 Count the number of rows and columns
print(len(df.index))
print(len(df.columns))
print(df.shape)

# Filter the titles which contain python
# Filter the titles which contain JavaScript
# Explore the data and make sense of it