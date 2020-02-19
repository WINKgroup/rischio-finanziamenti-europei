import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('Rischio-dei-finanziamenti.csv', delimiter=";")
df.columns = ['Anno', 'Regione', 'Tasso', 'Inutile']
df = df.drop('Inutile', axis=1)

tassoPerRegione = df.groupby(['Regione']).agg({'Tasso': 'mean'})
tassoPerAnno = df.groupby(['Anno']).agg({'Tasso': 'mean'})

plt.hist([tassoPerAnno['Tasso'], tassoPerRegione['Tasso']], bins=10, cumulative=True, density=True, label=['Per anno', 'Per regioni'])
plt.legend()
plt.title('CDF a confronto')
plt.xlabel('tasso di rischio')
plt.ylabel('distribuzione di probabilità')
plt.show()
