import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivos_problemas_graficos/pedos.csv")
print(df)

#creando el grafico
sns.lineplot(x="Fecha", y="Pedos", data=df)

#creando un punto en el momento de mas pedos
plt.plot("01-09",17,"o")

#mostrando el gráfico
plt.show()