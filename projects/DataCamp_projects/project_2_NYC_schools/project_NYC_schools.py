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
above_80 = schools[schools['average_math'] >= (800 * 0.8)]

