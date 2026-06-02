import dataframe as df

CONSUMO_AUTOCLAVE_1_2 = 200
CONSUMO_AUTOCLAVE_3 = 30
CONSUMO_TERMO = 80


def calcular_consumo(ciclos_por_maquina):

    resultado = {}

    for maquina, ciclos in ciclos_por_maquina.items():

        if maquina in ["AUTOCLAVE 1", "AUTOCLAVE 2"]:
            consumo = CONSUMO_AUTOCLAVE_1_2

        elif maquina in [
            "TERMODESINFECTORA 01",
            "TERMODESINFECTORA 02"
        ]:
            consumo = CONSUMO_TERMO

        else:
            consumo = CONSUMO_AUTOCLAVE_3

        resultado[maquina] = (
            ciclos * consumo
        ) / 1000

    return resultado