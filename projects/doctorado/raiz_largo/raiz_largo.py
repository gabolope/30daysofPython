import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

largo_raiz = pd.read_csv('projects/doctorado/raiz_largo/largo_raiz.csv')

# Hago un pivot de los datos para poder graficarlos:
columnas_dias = [str(i) for i in range(1, 16)]

largo_raiz = pd.melt(largo_raiz, id_vars=['genotipo', 'placa', 'experimento', 'id_planta'], value_vars = columnas_dias, var_name='dia', value_name='largo')

# Borro los NaN y cambio los str a float
largo_raiz = largo_raiz.replace('-', np.nan)
largo_raiz = largo_raiz.dropna()

largo_raiz['dia'] = pd.to_numeric(largo_raiz['dia'])
largo_raiz['largo'] = largo_raiz['largo'].astype(float)


# largo_raiz.to_csv('projects/doctorado/raiz_largo/largo_raiz_pivot.csv', index=False)

filtro_anormales = ((largo_raiz['dia'] >= 10 ) & (largo_raiz['largo'] < 10))

anormales = largo_raiz[filtro_anormales]['id_planta'].unique()
print(anormales)

# Hago gráfico
largo_raiz_14 = largo_raiz[largo_raiz['dia'] < 15] # saco el dia 15
g = sns.relplot(x='dia', y='largo', kind='line', data=largo_raiz_14, hue='genotipo', errorbar='sd')

plt.gca().invert_yaxis() #invierto el eje porque está al revés

# Nombres en los ejes
g.set(xlabel='Día', ylabel='Largo de raíz (mm)')
plt.xticks(ticks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
plt.ylim(0, None) # hago que la escala del y arranque en el 0

plt.show()