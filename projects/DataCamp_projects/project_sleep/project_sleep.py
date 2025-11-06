import pandas as pd

data = pd.read_csv('projects/DataCamp_projects/project_sleep/sleep_health_data.csv')

# Which occupation has the lowest average sleep duration? Save this in a string variable called lowest_sleep_occ.

occupation_duration = data.groupby('Occupation')['Sleep Duration'].mean().sort_values(ascending=True)
lowest_sleep_occ = occupation_duration.index[0]

print(lowest_sleep_occ) # Sales Representative


# Which occupation has the lowest average sleep quality? Save this in a string variable called lowest_sleep_quality_occ. Did the occupation with the lowest sleep duration also have the lowest sleep quality? If so assign a boolean value to variable same_occ variable, True if it is the same occupation, and False if it isn't.

occupation_quality = data.groupby('Occupation')['Quality of Sleep'].mean().sort_values(ascending=True)

lowest_sleep_quality_occ = occupation_quality.index[0] 

if lowest_sleep_occ == lowest_sleep_quality_occ:
  same_occ = True
else: 
  same_occ = False

print(lowest_sleep_quality_occ) # Sales Representative
print(same_occ) # True


# Let's explore how BMI Category can affect sleep disorder rates. Start by finding what ratio of app users in each BMI Category have been diagnosed with Insomnia. Create a dictionary named: bmi_insomnia_ratios. The key should be the BMI Category as a string, while the value should be the ratio of people in this category with insomnia as a float rounded to two decimal places. Here is an example:
""" 
bmi_insomnia_ratios = {
  'Normal': float,
  'Overweight': float,
  'Obese': float
  } 
"""
# Please note the keys are case-sensitive, and should be formatted as shown in the example dictionary.


bmi_categories = data['BMI Category'].unique()

bmi_insomnia_ratios = dict()

for bmi in bmi_categories:
  total = data[data['BMI Category'] == bmi]
  insomnia = total[total['Sleep Disorder'] == 'Insomnia']
  bmi_insomnia_ratios[bmi] = round(insomnia.shape[0]/total.shape[0], 2)

print(bmi_insomnia_ratios) # {'Overweight': 0.43, 'Normal': 0.04, 'Obese': 0.4}




