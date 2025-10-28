import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

largo_raiz = pd.read_csv('projects/doctorado/raiz_largo/largo_raiz.csv')

# Hago un pivot de los datos para poder graficarlos:
columnas_dias = [str(i) for i in range(1, 16)]

largo_raiz = pd.melt(largo_raiz, id_vars=['genotipo', 'placa', 'experimento', 'id_planta'], value_vars = columnas_dias, var_name='dia', value_name='largo')

# Borro los NaN
largo_raiz = largo_raiz.replace('-', np.nan)
largo_raiz = largo_raiz.dropna()

# Ajusto los types de las columnas
largo_raiz['dia'] = largo_raiz['dia'].astype(int)
largo_raiz['largo'] = largo_raiz['largo'].astype(float)
largo_raiz['id_planta'] = largo_raiz['id_planta'].astype(str)
largo_raiz['placa'] = largo_raiz['placa'].astype(str)

# Guardo el DF
# largo_raiz.to_csv('projects/doctorado/raiz_largo/largo_raiz_pivot.csv', index=False)

# Busco raíces anormales (largo menor de 10 después de los 10 días)
filtro_anormales = ((largo_raiz['dia'] >= 10 ) & (largo_raiz['largo'] < 10))
anormales = largo_raiz[filtro_anormales]

# quito las anormales del df largo_raiz
largo_raiz = largo_raiz[~filtro_anormales]

# Colores
paleta = [ "#5075B0",'#F25912']
sns.set_palette(paleta)

# Grafico
largo_raiz_14 = largo_raiz[largo_raiz['dia'] < 15] # saco el dia 15
g = sns.relplot(x='dia', y='largo', kind='line', data=largo_raiz_14, hue='genotipo', errorbar='sd')

# Ajustes
plt.xlabel('Dia')
plt.ylabel('Largo de raíz (mm)')
plt.xticks(ticks = range(1, 15))
plt.ylim(0, None)

new_labels = ['WT', 'SWAP A']
for t, l in zip(g._legend.texts, new_labels):
    t.set_text(l)

# Cambiar título, posición y marco
g._legend.set_title('Genotipo')
g._legend.set_frame_on(True)
g._legend.set_bbox_to_anchor((0.15, 0.95))  # posición dentro del gráfico
g._legend._loc = 2  # 'upper left'
plt.show()

# Muetro las plantas anormales unicos, sin repetir
anormales_unicos = anormales[['genotipo', 'placa', 'experimento', 'id_planta']].drop_duplicates()
g = sns.catplot(x='genotipo', kind='count', data=anormales_unicos, order=['wt', 'sa'])
g.set_xticklabels(['WT', 'SWAP A'])
plt.title('Plantas con crecimiento anormal')
plt.xlabel('Genotipo')
plt.ylabel('Número de plantas')
plt.show()
