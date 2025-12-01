# Are more goals scored in women's international soccer matches than men's?
# You assume a 10% significance level, and use the following null and alternative hypotheses:

# H0 : The mean number of goals scored in women's international soccer matches is the same as men's.
# HA : The mean number of goals scored in women's international soccer matches is greater than men's.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

alpha = 0.1

men_df = pd.read_csv('projects/DataCamp_projects/project_8_football/men_results.csv')
women_df = pd.read_csv('projects/DataCamp_projects/project_8_football/women_results.csv')

# filtro los partidos despues del 2002-01-01
men_df = men_df[men_df['date'] >= '2002-01-01']
women_df = women_df[women_df['date'] >= '2002-01-01']

# filtro los partidos de la FIFA Wolrd Cup
men_df = men_df[men_df['tournament'] == 'FIFA World Cup']
women_df = women_df[women_df['tournament'] == 'FIFA World Cup']

# hago una columna con el total de goles de cada partido
men_df['goals'] = men_df['home_score'] + men_df['away_score']
women_df['goals'] = women_df['home_score'] + women_df['away_score']

# miro la distribución de goles
sns.displot(data=men_df, x='goals', kind='kde', color='blue')
sns.displot(data=women_df, x='goals', kind='kde', color='red')
plt.show() # los datos no se ven normales

# hago un QQ plot para analizar si hay normalidad de manera preliminar
from statsmodels.graphics.gofplots import qqplot
from scipy.stats.distributions import norm
qqplot(men_df['goals'], line='s', dist=norm)
qqplot(women_df['goals'], line='s', dist=norm)
plt.show() # los puntos no se ajustan a la linea, no parecen normales

# hago un test de Shapiro-Wilk para definir si son o no normales
from scipy.stats import shapiro

stat_men, p_men = shapiro(men_df['goals'])
stat_women, p_women = shapiro(women_df['goals'])

# H0: los datos siguen una distribución normal
# HA: los datos NO siguen una distribución normal
if p_men > alpha:
  print(f'{p_men}, H0 no es rechazada. Los datos de hombres son normales')
else:
  print(f'{p_men}, H0 es rechazada. Los datos de hombres NO son normales')

if p_women > alpha:
  print(f'{p_women}, H0 no es rechazada. Los datos de mujeres son normales')
else:
  print(f'{p_women}, H0 es rechazada. Los datos de mujeres NO son normales')

# Resultado: los datos no son normales, hay que utilizar un test no paramétrico.

# hago test de Mann Whitney U
from scipy.stats import mannwhitneyu

u_stat, u_pval = mannwhitneyu(y=men_df['goals'], x=women_df['goals'], alternative='greater')

print('Valor P:', u_pval)
if u_pval > alpha:
  print('H0 no es rechazada. Los datos son iguales para hombres y mujeres')
  result = 'fail to reject'
else:
  print('H0 es rechazada, la media de goles de mujeres es mas alta.')
  result = 'reject'

# Hay diferencias entre hombres y mujeres

print('Promedio de goles en hombres:', men_df['goals'].mean())
print('Promedio de goles en mujeres:', women_df['goals'].mean())

result_dict ={'p_val': u_pval, 'result': result}
