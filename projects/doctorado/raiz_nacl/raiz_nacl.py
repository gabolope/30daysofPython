import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

raiz_nacl= pd.read_csv('projects/doctorado/raiz_nacl/raiz_nacl.csv', skiprows=1)

# Agrego columna de crecimiento (largo_raiz_final - largo_raiz_inicial)
raiz_nacl['crecimiento'] = raiz_nacl['largo_raiz_final'] - raiz_nacl['largo_raiz_inicial']

print(raiz_nacl.groupby(by='genotipo')['crecimiento'].mean())

# Busco los outliers
seventy_fifth = raiz_nacl['crecimiento'].quantile(0.75)
twenty_fifth = raiz_nacl['crecimiento'].quantile(0.25)
iqr =  seventy_fifth - twenty_fifth
upper = seventy_fifth + (1.5 * iqr)
lower = twenty_fifth - (1.5 * iqr)

outliers = raiz_nacl[(raiz_nacl['crecimiento'] < lower) | (raiz_nacl['crecimiento'] > upper)]
print(outliers)

# Quito la planta 24 para que el grafico se ajuste mejor
raiz_nacl = raiz_nacl[~(raiz_nacl['id_planta']==24)]

# Colores
paleta = [ "#5075B0",'#F25912']
sns.set_palette(paleta)

# Grafico el crecimiento: 
g = sns.catplot(kind='box', data=raiz_nacl, x='genotipo', y='crecimiento')

# Ajustes:
plt.xlabel('Genotipo')
plt.ylabel('Crecimiento (mm)')
g.set_xticklabels(['WT', 'SWAP A'])
plt.show()

g2 = sns.catplot(kind='count', data=raiz_nacl, x='genotipo', hue='supervivencia')
plt.show()