import pandas as pd
import glob
import os

ANO_PADRAO = "2025"

MAPA_MES_NUMERO = {
    "janeiro": "01",
    "fevereiro": "02",
    "março": "03",
    "abril": "04",
    "maio": "05",
    "junho": "06",
    "julho": "07",
    "agosto": "08",
    "setembro": "09",
    "outubro": "10",
    "novembro": "11",
    "dezembro": "12"
}

PASTA_DADOS = os.path.join(
    os.path.dirname(__file__),
    "dados"
)

arquivos = glob.glob(os.path.join(PASTA_DADOS, "*.xlsx"))

lista_dados = []

for arquivo in arquivos:

    df_temp = pd.read_excel(arquivo)

    df_longo = df_temp.melt(
        id_vars=["DATA"],
        var_name="DIA",
        value_name="CICLOS"
    )

    df_longo = df_longo.rename(columns={"DATA": "Máquina"})

    nome_arquivo = os.path.basename(arquivo)
    mes = nome_arquivo.replace(".xlsx", "").lower()

    df_longo["Mes"] = mes

    lista_dados.append(df_longo)

if not lista_dados:
    raise FileNotFoundError(
        f"Nenhuma planilha .xlsx encontrada em: {PASTA_DADOS}"
    )

dados = pd.concat(lista_dados, ignore_index=True)

dados["CICLOS"] = dados["CICLOS"].fillna(0)

dados["Mes"] = dados["Mes"].astype(str).str.strip().str.lower()

dados["Mes_num"] = dados["Mes"].map(MAPA_MES_NUMERO)

dados["AnoMes"] = ANO_PADRAO + "-" + dados["Mes_num"]

dados["Data_sort"] = pd.to_datetime(
    dados["AnoMes"] + "-01",
    errors="coerce"
)

dados = dados.sort_values("Data_sort")


def obter_meses_disponiveis():
    return sorted(dados["AnoMes"].dropna().unique().tolist())


def obter_maquinas(df_base=None):
    base = df_base if df_base is not None else dados
    return sorted(base["Máquina"].unique().tolist())


def filtrar_dados(mes="Todos", maquina="Todas"):
    df_base = dados.copy()

    if mes != "Todos":
        df_base = df_base[df_base["AnoMes"] == mes]

    if maquina and maquina != "Todas":
        df_base = df_base[df_base["Máquina"] == maquina]

    return df_base

total_ciclos_periodo = (
    dados.groupby("Máquina")["CICLOS"]
    .sum()
    .to_dict()
)

total_ciclos_mensais = (
    dados.groupby(["Máquina", "Mes"])["CICLOS"]
    .sum()
    .to_dict()
)