# 1 Get the current day, month, year, hour, minute and timestamp from datetime module
from datetime import datetime
now = datetime.now()
print("#1:", now) # 2025-06-23 14:59:25.300242

# 2 Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
now = now.strftime('%m/%d/%Y, %H:%M:%S')
print("#2:", now) # 06/23/2025, 15:01:11

# 3 Today is 5 December, 2019. Change this time string to time.
date_str = 'Today is 5 December, 2019.'
date_object = datetime.strptime(date_str, 'Today is %d %B, %Y.')
print("#3:", date_object) # 2019-12-05 00:00:00

# 4 Calculate the time difference between now and new year.
new_year = datetime(2026, 1, 1)
now = datetime.now()
time_left = new_year - now
print("#4: THe time left to new year is", time_left)

# 5 Calculate the time difference between 1 January 1970 and now.
print("#5: difference in seconds", now.timestamp())

# 6 Think, what can you use the datetime module for? Examples:
#   Time series analysis
#   To get a timestamp of any activities in an application
# Cuando se realiza una compra en una app, la funcion que realiza la compra toma un timestamp que guarda con el resto de la información.
#   Adding posts on a blog

