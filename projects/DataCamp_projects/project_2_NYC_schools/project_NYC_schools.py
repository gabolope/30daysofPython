# Importar las librerías
import matplotlib as plt
import pandas as pd
import numpy as np

# Leer el archivo csv:
schools = pd.read_csv('projects\DataCamp_projects\project_2_NYC_schools\schools.csv')

# Mirar los datos
# print(schools.head())

# Which NYC schools have the best math results?
# The best math results are at least 80% of the *maximum possible score of 800* for math.
# Save your results in a pandas DataFrame called best_math_schools, including "school_name" and "average_math" columns, sorted by "average_math" in descending order.
above_80 = schools[schools['average_math'] > 800 * 0.8]

best_math_schools = above_80.loc[:, ['school_name', 'average_math']].sort_values('average_math', ascending=False)
print(best_math_schools)

# What are the top 10 performing schools based on the combined SAT scores?
# Save your results as a pandas DataFrame called top_10_schools containing the "school_name" and a new column named "total_SAT", with results ordered by "total_SAT" in descending order ("total_SAT" being the sum of math, reading, and writing scores).
schools['total_SAT'] = schools['average_math'] + schools['average_writing'] + schools['average_reading']
top_10_schools_complete = schools.sort_values('total_SAT', ascending=False)[:10]
top_10_schools = top_10_schools_complete.loc[:, ['school_name', 'total_SAT']]
print(top_10_schools)

# Which single borough has the largest standard deviation in the combined SAT score?
# Save your results as a pandas DataFrame called largest_std_dev.
# The DataFrame should contain one row, with:
# "borough" - the name of the NYC borough with the largest standard deviation of "total_SAT".
# "num_schools" - the number of schools in the borough.
# "average_SAT" - the mean of "total_SAT".
# "std_SAT" - the standard deviation of "total_SAT".
# Round all numeric values to two decimal places.

# Agrupo por borough, calculo el std de SAT para cada grupo, ordeno en base al std 
borough_std = top_10_schools_complete.groupby('borough')['total_SAT'].std().sort_values(ascending=False)

# Quito el índex para acceder al nombre del primer elemento de la lista
borough_std = borough_std.reset_index()

# Tomo el primer elemento de la lista, 
borough = borough_std.iloc[0,0]
print(borough)

# Realizo el conteo de cuántas escuelas hay por distrito, luego selecciono al distrito que tiene más std.
num_schools = schools['borough'].value_counts().loc[borough]
print(num_schools)

# Calculo el promedio de total_SAT de todas las escuelas
average_SAT = schools.groupby('borough')['total_SAT'].mean().__round__(2).loc[borough]
print(average_SAT)

# Calculo el std de SAT de todas las escuelas. 
std_SAT = schools.groupby('borough')['total_SAT'].std().__round__(2).loc[borough]
print(std_SAT)

# Creo un dictionary para pasarlo a DF
data = {
  'borough': [borough],
  'num_schools': [num_schools],
  'average_SAT':[ average_SAT],
  'std_SAT': [std_SAT]
}

largest_std_dev = pd.DataFrame(data)
print(largest_std_dev)