import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./NA Parameters.csv', sep=',', header=0, index_col=0)
df.columns = [col.lstrip('">') for col in df.columns]
print(df)


pd.plotting.scatter_matrix(df.iloc[:, 6:12], alpha=0.2)
plt.plot(range(1000))
plt.show()


import plotly.express as px
fig = px.scatter_matrix(df,
    dimensions=['shear', 'stretch', 'stagger', 'buckle', 'propeller', 'opening'],
    title="Scatter matrix of certain parameters describing base pairs in 8GLP structure"
    )
fig.update_traces(diagonal_visible=False)
fig.show()


import seaborn as sns
sns.set_theme(style="ticks")
sns.pairplot(df.iloc[:, 6:12])
plt.show()