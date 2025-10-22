import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

crimes = pd.read_csv('projects/DataCamp_projects/project_4_crime/crimes.csv')

# Which hour has the highest frequency of crimes? Store as an integer variable called peak_crime_hour.

# paso la hora militar a str. zfill hace que todos los horarios tengan 4 caracteres de largo para poder ser formateados
crimes['hour'] = pd.to_datetime(crimes['TIME OCC'].astype(str).str.zfill(4), format='%H%M').dt.hour

peak_crime_hour = crimes['hour'].value_counts().index[0]
print(f'La hora con más crímenes es: {peak_crime_hour}:00 hrs')


# Which area has the largest frequency of night crimes (crimes committed between 10pm and 3:59am)? Save as a string variable called peak_night_crime_location.

#hago un listado de las horas nocturnas y filtro en base a eso. 
night = [22, 23, 24, 0, 1, 2, 3]

crimes_night = crimes[crimes['hour'].isin(night)]
print(crimes_night.head())

peak_night_crime_location = crimes_night['AREA NAME'].value_counts().index[0]
print(f'El área con más crímenes nocturnos es: {peak_night_crime_location}')


# Identify the number of crimes committed against victims of different age groups. Save as a pandas Series called victim_ages, with age group labels "0-17", "18-25", "26-34", "35-44", "45-54", "55-64", and "65+" as the index and the frequency of crimes as the values.

labels = ['0-17', '18-25', '26-34', '35-44', '45-54', '55-64', '65+']
max_age = crimes['Vict Age'].max()
bins = [0, 17, 25, 34, 44, 54, 64, max_age]

crimes['age_group'] = pd.cut(crimes['Vict Age'], labels=labels, bins=bins)

victim_ages = crimes['age_group'].value_counts()
print(victim_ages)
sns.histplot(data=crimes, x='age_group')
plt.show()