import streamlit as st
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(
    page_title='Relatório',
    page_icon=':a:',
    layout='wide'
)

df = pd.read_csv("Vendas 2024 - 2025.xlsx - Vendas.csv", engine= 'python')

   # Converter a coluna de data para datetime (formato correto)
df["DATA_VENDA"] = pd.to_datetime(df["DATA_VENDA"], dayfirst=True)
   #converte o valor da venda de str para float
df["VALOR_VENDA"] = df["VALOR_VENDA"].str.replace(",", ".").astype(float)

with st.sidebar:
   st.image('data:image/png;base64,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')
st.sidebar.header("Filtros")

   # Filtrar por filial
filiais = df["FILIAL"].unique()
filial_selecionada = st.sidebar.selectbox("Selecione a Filial", filiais)

   # Filtrar por data
data_min = df["DATA_VENDA"].min()
data_max = df["DATA_VENDA"].max()
data_inicial, data_final = st.sidebar.date_input("Selecione o Período", [data_min, data_max], data_min, data_max)
   # Converter as datas para o formato do dataframe
data_inicial = pd.to_datetime(data_inicial)
data_final = pd.to_datetime(data_final)

   # Aplicar filtros
df_filtrado = df[(df["FILIAL"] == filial_selecionada) & (df["DATA_VENDA"].between(data_inicial, data_final))]

   # Agrupar os valores por data (caso tenha múltiplas vendas no mesmo dia)
df_filtrado = df_filtrado.groupby("DATA_VENDA")["VALOR_VENDA"].sum().reset_index()

#soma dos valores por filia, mudar pra ser por filial e por mes pra saber quanto ja foi vendido nesse mes
#df_filial_soma = df[df["FILIAL"] == 2]  # Filtrando a filial 0001
#total_vendas = df_filial_soma["VALOR_VENDA"].sum()

   #soma das vendas do dia do relatório por filial
data_referencia = pd.to_datetime(datetime.date.today())
df_filial_soma_dia = df[(df["FILIAL"] == filial_selecionada) & (df["DATA_VENDA"] == data_referencia)]
total_vendas_dia = df_filial_soma_dia["VALOR_VENDA"].sum()

   #exibir soma das vendas do mês no ano aterior
data_atual = pd.to_datetime(datetime.date.today())
dia_atual = data_atual.day
mes_anterior = data_atual.month
ano_anterior = data_atual.year - 1
df_mes_anterior = df[(df["FILIAL"] == filial_selecionada) &
                     (df["DATA_VENDA"].dt.month == mes_anterior) & 
                     (df["DATA_VENDA"].dt.year == ano_anterior)]

total_vendas_mes_anterior = df_mes_anterior["VALOR_VENDA"].sum()


   #meta de vendas do mês
porcetagem_meta = total_vendas_mes_anterior * 0.05
meta_venda_mês = porcetagem_meta + total_vendas_mes_anterior
print(porcetagem_meta, meta_venda_mês)

   #meta x resultado 
# Filtrar dados do mês e filial
df_filial = df[(df["FILIAL"] == filial_selecionada) & 
               (df["DATA_VENDA"].dt.month == data_atual.month) & 
               (df["DATA_VENDA"].dt.year == data_atual.year) & 
               (df["DATA_VENDA"].dt.day <= data_atual.day)]  # Apenas até o dia atual

vendas_realizadas = df_filial["VALOR_VENDA"].sum()
meta_vendas = meta_venda_mês

#previsão de vendas 
previsao = (vendas_realizadas / data_atual.day) * 30


# Criar gráfico de comparação Meta x Previsão x Vendas
fig, ax = plt.subplots(figsize=(8, 3))
categorias = ["Meta","Previsão", "Realizado"]
valores = [meta_vendas, previsao, vendas_realizadas]

ax.bar(categorias, valores, color=["gray","blue", "red" ])
ax.set_title(f"Comparação Meta x Previsão x Vendas - {dia_atual}/{mes_anterior}/{ano_anterior + 1}")
ax.set_ylabel("Valor (R$)")

# Exibir os dados filtrados
def divisor():
   st.markdown("<hr style='border: 2px solid #ccc;'>", unsafe_allow_html=True)

#cabeçalho
st.write(f"# Relatório meta de venda loja {dia_atual}/{mes_anterior}/{ano_anterior + 1}")

divisor()

#col1, col2, col3 = st.columns(3)

col1, col2 = st.columns(2)

with col1:
   st.write(f"""#### Total de vendas em {mes_anterior}/{ano_anterior}: \n 
            R$ {total_vendas_mes_anterior:,.2f}
            """)
with col2:
   st.write(f"""#### Total das vendas de hoje por filial: \n
            R$ {total_vendas_dia:,.2f}
            """)
#with col3:
#   st.write(f"""#### A meta de venda do mês é: \n 
#            R$ {meta_venda_mês:,.2f}""") 
   
divisor()

#grafico Meta x Previsão x Vendas
st.pyplot(fig)
st.write(f"**Meta de vendas:** R$ {meta_vendas:,.2f}")
st.write(f"**Previsão de vendas:** R$ {previsao:,.2f}")
st.write(f"**Vendas realizadas:** R$ {vendas_realizadas:,.2f}")

divisor()

#st.write(f" {total_vendas}")
st.write("### Gráfico de vendas por periodo")
st.line_chart(df_filtrado.set_index("DATA_VENDA")["VALOR_VENDA"])   

st.dataframe(df_filtrado)
