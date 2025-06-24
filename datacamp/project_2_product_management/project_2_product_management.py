import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

workout_df = pd.read_csv('datacamp/project_2_product_management/workout.csv')
print(workout_df)
# When was the global search for 'workout' at its peak? Save the year of peak interest as a string named year_str in the format "yyyy".

# primero, hago una columna con todos los años sin tener en cuenta el mes. 
def year_filter(year_month):
    year_month_obj = datetime.strptime(year_month, '%Y-%m')
    return year_month_obj.year

workout_df['year'] = workout_df['month'].apply(year_filter)

print(workout_df)
