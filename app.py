import streamlit as st
import pandas as pd
import os

import dataframe as df
import consumo_agua as ca
import gasto_financeiro as gf

st.set_page_config(
    page_title="Rede Hospitalar | Centro de Operações CME",
    layout="wide"
)


st.markdown("""
<style>

.main {
    background-color: #F5F7FA;
}

[data-testid="stMetric"] {
    background-color: #0000;
    padding: 14px;
    border-radius: 14px;
    border: 1px solid #E6EAF0;
    border-left: 6px solid #0070D1;
}

h1, h2, h3, h4 {
    color: #003B7A;
}

</style>
""", unsafe_allow_html=True)

logo_path = os.path.join(
    os.path.dirname(__file__),
    "RDOR3.SA_BIG-93ed1ffc.png"
)

col_logo, col_titulo = st.columns(
    [1, 8],
    vertical_alignment="center"
)

with col_logo:
    if os.path.exists(logo_path):
        st.image(logo_path, width=55)

with col_titulo:
    st.markdown(
        "<h4 style='margin-bottom:0;'>Rede Hospitalar | Centro de Operações CME</h4>",
        unsafe_allow_html=True
    )
    st.caption(
        "Monitoramento de produtividade, consumo de água e custos operacionais"
    )


meses_disponiveis = df.obter_meses_disponiveis()

opcoes = ["Todos"] + meses_disponiveis

mes_selecionado = st.sidebar.selectbox(
    "Selecione o período (Ano-Mês)",
    opcoes
)

# filtro inicial
df_base = df.filtrar_dados(
    mes=mes_selecionado
)

maquinas_disponiveis = df.obter_maquinas(df_base)

maquina_selecionada = st.sidebar.selectbox(
    "Selecione a máquina",
    ["Todas"] + maquinas_disponiveis
)

# filtro final
df_base = df.filtrar_dados(
    mes=mes_selecionado,
    maquina=maquina_selecionada
)


ciclos_filtrados = df_base.groupby("Máquina")["CICLOS"].sum()

consumo_agua = pd.Series(
    ca.calcular_consumo(ciclos_filtrados.to_dict())
)

custos = pd.Series(
    gf.calcular_custo(consumo_agua.to_dict())
)

total_ciclos = ciclos_filtrados.sum()
total_agua = consumo_agua.sum()
total_custo = custos.sum()

maquina_mais_utilizada = (
    ciclos_filtrados.idxmax()
    if len(ciclos_filtrados) > 0
    else "-"
)

st.markdown("### Indicadores Operacionais")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Total de Ciclos", int(total_ciclos))

with c2:
    st.metric("Consumo de Água", f"{total_agua:.2f} m³")

with c3:
    st.metric("Custo Estimado", f"R$ {total_custo:.2f}")

with c4:
    st.metric("Máquina Líder", maquina_mais_utilizada)

st.divider()

st.markdown("### Análises Operacionais")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Ciclos por Máquina")
    st.bar_chart(
        ciclos_filtrados
    )

with col2:
    st.subheader("Consumo por Máquina")
    st.bar_chart(consumo_agua)

col3, col4 = st.columns(2)

with col3:
    st.subheader("Custo por Máquina")
    st.bar_chart(custos)

with col4:
    st.subheader("Evolução dos Ciclos")
    st.line_chart(
        df.dados.groupby("AnoMes")["CICLOS"].sum()
    )

st.divider()

base_maquina = gf.calcular_metricas_financeiras(df_base).reset_index()


tab1, tab2 = st.tabs(["📊 Resumo por Máquina", "📂 Base Bruta"])

with tab1:

    resumo = base_maquina[
        [
            "ciclos",
            "consumo_m3",
            "custo_total",
            "operacao_%",
            "custo_por_ciclo",
            "consumo_por_ciclo"
        ]
    ].sort_values("ciclos", ascending=False)

    st.dataframe(
        resumo.rename(columns={
            "ciclos": "Ciclos",
            "consumo_m3": "Consumo (m³)",
            "custo_total": "Custo (R$)",
            "operacao_%": "Participação (%)",
            "custo_por_ciclo": "Custo/Ciclo",
            "consumo_por_ciclo": "Consumo/Ciclo"
        }).style.format({
            "Ciclos": "{:.0f}",
            "Consumo (m³)": "{:.2f}",
            "Custo (R$)": "R$ {:.2f}",
            "Participação (%)": "{:.2f}%",
            "Custo/Ciclo": "R$ {:.2f}",
            "Consumo/Ciclo": "{:.2f}"
        }),
        use_container_width=True
    )

with tab2:

    df_base_ordenado = df_base.sort_values(
        by=["AnoMes", "Máquina"],
        ascending=[True, True]
    )

    df_base_ordenado = df_base_ordenado.merge(
        base_maquina,
        on="Máquina",
        how="left"
    )

    colunas_base = ["Máquina", "CICLOS", "Mes", "AnoMes"]

    colunas_metricas = [
        "consumo_m3",
        "custo_total",
        "operacao_%",
        "custo_por_ciclo",
        "consumo_por_ciclo"
    ]

    st.dataframe(
        df_base_ordenado[colunas_base + colunas_metricas],
        use_container_width=True,
        hide_index=True
    )
