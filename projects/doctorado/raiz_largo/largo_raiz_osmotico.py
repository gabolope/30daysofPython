import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

largo_raiz = pd.read_csv('projects/doctorado/raiz_largo/largo_raiz_osmotico.csv')

# Hago un pivot de los datos para poder graficarlos:
columnas_dias = [str(i) for i in range(1, 9)]

largo_raiz = pd.melt(largo_raiz, id_vars=['genotipo', 'placa', 'experimento', 'id_planta'], value_vars = columnas_dias, var_name='dia', value_name='largo')

# Borro los NaN
largo_raiz = largo_raiz.replace('-', np.nan)
largo_raiz = largo_raiz.dropna()

# Ajusto los types de las columnas
largo_raiz['dia'] = largo_raiz['dia'].astype(int)
largo_raiz['largo'] = largo_raiz['largo'].astype(float)
largo_raiz['id_planta'] = largo_raiz['id_planta'].astype(str)
largo_raiz['placa'] = largo_raiz['placa'].astype(str)

# Grafico de lineas:
g = sns.relplot(kind='line', data=largo_raiz, x='dia', y='largo', hue='genotipo', errorbar='sd')
# Nombres en los ejes
plt.xlabel('Dia')
plt.ylabel('Largo de raíz (mm)')
# Ticks del x
plt.xticks(ticks = range(1, 9))

# Cambiar los nombres de la leyenda (manteniendo colores correctos)
new_labels = ['WT', 'SWAP A']
for t, l in zip(g._legend.texts, new_labels):
    t.set_text(l)

# Cambiar título, posición y marco
g._legend.set_title('Genotipo')
g._legend.set_frame_on(True)
g._legend.set_bbox_to_anchor((0.15, 0.95))  # posición dentro del gráfico
g._legend._loc = 2  # 'upper left'

# hago que la escala Y arranca en el 0
plt.ylim(0, None)
plt.show()