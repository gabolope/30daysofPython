# Which airlines and routes (for example "PDX-SFO") are most affected by flight delays, and what impact does wind have on departure delays?

# Load the two CSV files into separate DataFrames. Explore the data and create any new columns that might benefit your analysis.

import pandas as pd

flights = pd.read_csv('projects/project_flight_delays/flights2022.csv')
weather = pd.read_csv('projects/project_flight_delays/flights_weather2022.csv')

# print(flights.columns) # 20 columnas: 'year', 'month', 'day', 'dep_time', 'sched_dep_time', 'dep_delay',
#                                    'arr_time', 'sched_arr_time', 'arr_delay', 'carrier', 'flight',
#                                 'tailnum', 'origin', 'dest', 'air_time', 'distance', 'hour', 'minute',
#                               'time_hour', 'airline'


# print(weather.columns) # 29 columnas: 'year', 'month', 'day', 'dep_time', 'sched_dep_time', 'dep_delay',
                      #       'arr_time', 'sched_arr_time', 'arr_delay', 'carrier', 'flight',
                      #       'tailnum', 'origin', 'dest', 'air_time', 'distance', 'hour', 'minute',
                      #       'airline', 'route', 'temp', 'dewp', 'humid', 'wind_dir', 'wind_speed',
                      #       'wind_gust', 'precip', 'pressure', 'visib'

# Creo una columna: route, única para cada combinación origin-dest
flights['route'] = flights['origin'] + '-' + flights['dest']


# For routes, calculate the average departure delays and highest number of canceled flights and store this as a DataFrame called routes_delays_cancels, resetting the index after calculating.

route_delay = flights.groupby(by='route')['dep_delay'].mean()
print(route_delay.head())
import this
# For airlines, determine the average departure delays and the highest number of canceled flights and store this as a DataFrame called airlines_delays_cancels, resetting the index after calculating.

# Produce two bar graphs to show (1) the top 9 highest number of cancellations by route in a plot called top9_route_cancels_bar and (2) the top 9 highest average departure delays by airline in a plot called top9_airline_delays_bar.

# Determine if 10 mile per hour wind gusts or more have a larger average departure delay for both of SEA and PDX, setting wind_response to True if so and False if not.