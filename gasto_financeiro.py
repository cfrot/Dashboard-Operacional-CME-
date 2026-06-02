import pandas as pd
import consumo_agua as ca

TARIFA_AGUA = 44.41


def calcular_custo(consumo_por_maquina):

    resultado = {}

    for maquina, consumo_m3 in consumo_por_maquina.items():

        resultado[maquina] = (
            consumo_m3 * TARIFA_AGUA
        )

    return resultado


def calcular_metricas_financeiras(df_base):

    base_maquina = (
        df_base.groupby("Máquina")
        .agg(
            ciclos=("CICLOS", "sum"),
            registros=("CICLOS", "count")
        )
    )

    consumo_map = ca.calcular_consumo(
        base_maquina["ciclos"].to_dict()
    )

    custo_map = calcular_custo(
        consumo_map
    )

    base_maquina["consumo_m3"] = (
        base_maquina.index.map(consumo_map)
    )

    base_maquina["custo_total"] = (
        base_maquina.index.map(custo_map)
    )

    total_ciclos = base_maquina["ciclos"].sum()

    if total_ciclos > 0:
        base_maquina["operacao_%"] = (
            base_maquina["ciclos"] / total_ciclos
        ) * 100
    else:
        base_maquina["operacao_%"] = 0

    base_maquina["custo_por_ciclo"] = (
        base_maquina["custo_total"] /
        base_maquina["ciclos"]
    ).fillna(0)

    base_maquina["consumo_por_ciclo"] = (
        base_maquina["consumo_m3"] /
        base_maquina["ciclos"]
    ).fillna(0)

    return base_maquina