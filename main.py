import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Finanças",
    page_icon=":moneybag:",
)
st.markdown("""
# Boas Vindas!

## Nosso APP Financeiro! 
         
Espero que você curta a experiência da nossa solução para organização financeira.            
            
""")
# Widget de upload de dados
file_upload = st.file_uploader(label = "Faça upload dos dados aqui", type = ["csv"])

# Verifica se o arquivo foi carregado e exibe o DataFrame
if file_upload:
    # Leitura de dados
    df = pd.read_csv(file_upload)
    df["Data"] = pd.to_datetime(df["Data"], format="%d/%m/%Y").dt.date


    # Exibição dos dados no App
    exp1 = st.expander("Dados Brutos")
    columns_fmt = {"Valor":st.column_config.NumberColumn("Valor", format = "R$ %.2f") }
    exp1.dataframe(df, hide_index= True,column_config=columns_fmt
    )

    # Visão Instituição
    exp2 = st.expander("Instituições")
    df_instituicao = df.pivot_table(index = "Data", columns="Instituição", values = "Valor")

    # Abas para diferentes visualizações
    tab_data, tab_history, tb_share = exp2.tabs(["Dados", "Histórico", "Distribuição"])

    # Exibe o dataframe
    tab_data.dataframe(df_instituicao)

    # Exibe o histórico
    with tab_history:    
        st.line_chart(df_instituicao)
    
    # Exibe a distribuição
    with tb_share:
        
        # Cria um seletor de data
        date = st.selectbox("Selecione uma data", options = df_instituicao.index)
        # Gráfico de distribuição
        st.bar_chart(df_instituicao.loc[date])

# Não tem arquivos...