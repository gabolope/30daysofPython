import numpy as np
import pandas as pd
from thefuzz import process

price = pd.read_csv('projects/DataCamp_projects/project_6_airbnb/airbnb_price.csv')
last_review = pd.read_csv('projects/DataCamp_projects/project_6_airbnb/airbnb_last_review.tsv', sep='\t')
room_type = pd.ExcelFile('projects/DataCamp_projects/project_6_airbnb/airbnb_room_type.xlsx')
room_type = room_type.parse('airbnb_room_type')

# What are the dates of the earliest and most recent reviews? Store these values as two separate variables with your preferred names.
last_review['last_review'] = pd.to_datetime(last_review['last_review'])
earliest = last_review['last_review'].min() # April 01 2019
most_recent = last_review['last_review'].max() # May 31 2019

print(type(earliest))
print(earliest)
print(most_recent)

# How many of the listings are private rooms? Save this into any variable.
print(room_type['room_type'].unique())
# Hago limpieza con thefuzz
room_list = ['entire home/apt', 'private room', 'shared room']

for room in room_list:
  matches = process.extract(room, room_type['room_type'], limit=room_type.shape[0])
  for potential_match in matches:
    if potential_match[1] >= 90:
      room_type.loc[room_type['room_type'] == potential_match[0], 'room_type'] = room

print(room_type['room_type'].unique()) # ahora estan los datos limpios

private_rooms = (room_type['room_type'].value_counts())['private room'] # 11356

# What is the average listing price? Round to the nearest two decimal places and save into a variable.
price['price'] = price['price'].str.replace(' dollars', '')
price['price'] = price['price'].astype(int)

average_price = round(price['price'].mean(), 2) # 141.78

# Combine the new variables into one DataFrame called review_dates with four columns in the following order: first_reviewed, last_reviewed, nb_private_rooms, and avg_price. The DataFrame should only contain one row of values.
result_dict = {'first_reviewed': [earliest], 'last_reviewed': [last_review], 'nb_private_rooms': [private_rooms], 'avg_price': [average_price]}

review_dates = pd.DataFrame(result_dict)
print(review_dates)