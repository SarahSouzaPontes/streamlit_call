import streamlit as st
import pandas as pd

# Carregando os dados do arquivo CSV
data = 'Call.csv'
df = pd.read_csv(data)

# Convertendo a coluna "Answer Rate" para um valor decimal
df['Answer Rate'] = df['Answer Rate'].str.rstrip('%').astype(float) / 100

# Criando uma coluna "Answer Rate AVG" corretamente
ans_rate_avg = df['Answer Rate'].mean()

# Criando uma tabela com 3 colunas para métricas
col1, col2, col3 = st.columns(3)

# Exibindo métricas
col1.metric("Incoming Calls AVG", round(df['Incoming Calls'].mean(), 2))
col2.metric("Answered Calls AVG", round(df['Answered Calls'].mean(), 2))
col3.metric("Answer Rate AVG", round(ans_rate_avg, 2))

# Gráfico de linha para "Incoming Calls" e "Answered Calls"
st.line_chart(df[['Incoming Calls', 'Answered Calls']])