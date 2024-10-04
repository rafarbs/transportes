import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('transporte_publico.csv')

print("Visão geral dos dados:")
print(df.head())

print("\nResumo estatístico:")
print(df.describe())

plt.figure(figsize=(10, 6))
sns.countplot(x='tipo_veiculo', data=df, palette='viridis')
plt.title('Distribuição dos Tipos de Veículos no Transporte Público')
plt.xlabel('Tipo de Veículo')
plt.ylabel('Quantidade')
plt.show()

plt.figure(figsize=(10, 6))
sns.lineplot(x='horario', y='num_passageiros', data=df, marker='o')
plt.title('Número de Passageiros por Horário')
plt.xlabel('Horário')
plt.ylabel('Número de Passageiros')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

df_lotacao = df.groupby('linha_onibus')['num_passageiros'].mean().reset_index()
df_lotacao = df_lotacao.sort_values(by='num_passageiros', ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(x='linha_onibus', y='num_passageiros', data=df_lotacao, palette='coolwarm')
plt.title('Média de Passageiros por Linha de Ônibus')
plt.xlabel('Linha de Ônibus')
plt.ylabel('Média de Passageiros')
plt.xticks(rotation=90)
plt.show()