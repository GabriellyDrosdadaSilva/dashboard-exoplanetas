import pandas as pd
import streamlit as st

df = pd.read_csv("data/exoplanetas.csv", comment="#")
print(df.shape)
print(df.head())
print(df.isna().sum())





##1. CONFIGURAR A PÁGINA
 #  definir título e layout da página
st.set_page_config(page_title="Exoplanetas", page_icon="🪐", layout="wide")

#2. CARREGAR OS DADOS
  # ler data/exoplanetas.csv (ignorando as linhas de comentário)
   #guardar em cache, para não reler a cada interação

#3. LIMPAR OS DADOS
 #  manter só as colunas úteis
  # remover linhas sem ano de descoberta ou sem método
   #converter o ano para número inteiro

#4. CRIAR OS FILTROS (barra lateral)
 #  filtro de intervalo de anos: do menor ao maior ano da tabela
  # filtro de métodos: lista de métodos, todos marcados por padrão

#5. APLICAR OS FILTROS
 #  df_filtrado = linhas onde
  #     o ano está dentro do intervalo escolhido
   #    E o método está entre os selecionados

#6. MOSTRAR O CONTADOR
 #  exibir o número de linhas de df_filtrado (total de planetas)

#7. GRÁFICO 1: descobertas por ano
 #  contar planetas por ano em df_filtrado
  # desenhar gráfico de linha (ano × quantidade)

#8. GRÁFICO 2: métodos de descoberta
 #  contar planetas por método em df_filtrado
  # desenhar gráfico de barras (método × quantidade)

#9. GRÁFICO 3: tamanho × distância
 #  remover linhas sem raio ou sem distância
  # desenhar dispersão (distância × raio do planeta)
   #colorir os pontos pelo método de descoberta
   #mostrar o nome do planeta ao passar o mouse

#10. (OPCIONAL) mostrar a tabela de dados filtrados

