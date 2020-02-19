import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Rischio-dei-finanziamenti.csv', delimiter=";")
df.columns = ['Anno', 'Regione', 'Tasso', 'Inutile']
df = df.drop('Inutile', axis=1)

df1997 = df[df['Anno'] == 1997]
df2013 = df[df['Anno'] == 2013]
df = df1997.append(df2013)

plt.title('Anni a confronto')
plt.xlabel('Anni')
plt.ylabel('Rischio percentuale')

sns.boxplot(x='Anno', y='Tasso', data=df)
plt.show()
