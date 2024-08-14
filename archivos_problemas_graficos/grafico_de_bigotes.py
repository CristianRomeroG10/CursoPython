import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivos_problemas_graficos/bigotes.csv")
print(df)

#creando el grafico
sns.boxplot(x="categorias", y="valor", data=df)

#mostrando el gráfico
plt.show()