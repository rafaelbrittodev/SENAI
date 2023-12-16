import matplotlib.pyplot as plt
import seaborn as sns

dados = sns.load_dataset('titanic')

sns.swarmplot(x='class', y='age', data=dados)


print(dados.head())
plt.show()