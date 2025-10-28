import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

raiz_lateral = pd.read_csv('projects/doctorado/raiz_lateral/raiz_lateral.csv')

# Pivot de la tabla con melt:
columnas_dias = [str(i) for i in range(1, 16)]

raiz_lateral = pd.melt(raiz_lateral, id_vars=['genotipo', 'placa', 'experimento', 'id_planta'], value_vars = columnas_dias, var_name='dia', value_name='laterales')

# Borro los NaN
raiz_lateral = raiz_lateral.replace('-', np.nan)
raiz_lateral = raiz_lateral.dropna()

# Ajusto los types de las columnas
raiz_lateral['dia'] = raiz_lateral['dia'].astype(int)
raiz_lateral['laterales'] = raiz_lateral['laterales'].astype(int)
raiz_lateral['id_planta'] = raiz_lateral['id_planta'].astype(str)
raiz_lateral['placa'] = raiz_lateral['placa'].astype(str)

# Quito plantas que nunca obtuvieron raices
filtro_anormales = ((raiz_lateral['dia'] >= 10 ) & (raiz_lateral['laterales'] < 3))
raiz_lateral = raiz_lateral[~filtro_anormales] 

# Colores
paleta = [ "#5075B0",'#F25912']
sns.set_palette(paleta)

# Grafico
g = sns.relplot(kind='line', data=raiz_lateral, x='dia', y='laterales', hue='genotipo', errorbar='sd')

# Ajustes:
plt.xlabel('Dia')
plt.ylabel('Número de raíces laterales')
plt.xticks(ticks = range(1, 16))
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