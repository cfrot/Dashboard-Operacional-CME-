# Dashboard Operacional CME

Sistema de monitoramento operacional desenvolvido em **Streamlit**, com foco em análise de produtividade, consumo de água e custos operacionais de equipamentos hospitalares (CME).

---

## Visão Geral

Este projeto tem como objetivo centralizar e visualizar indicadores operacionais de máquinas utilizadas no processo de esterilização hospitalar, permitindo:

* Análise de ciclos por máquina
* Cálculo de consumo de água estimado
* Estimativa de custos operacionais
* Comparação de performance entre equipamentos
* Visualização temporal da operação

---

## Principais Métricas

*  **Total de Ciclos**
*  **Consumo de Água (m³)**
*  **Custo Operacional Estimado**
*  **Máquina mais utilizada**
*  **Participação operacional (%)**
*  **Consumo por ciclo**
*  **Custo por ciclo**

---

##  Arquitetura do Projeto

O projeto foi estruturado em módulos para separar responsabilidades:

```
dashboard-cme-bigdata/
│
├── app.py                  # Interface principal (Streamlit)
├── dataframe.py            # Processamento e tratamento dos dados
├── consumo_agua.py        # Regras de cálculo de consumo
├── gasto_financeiro.py    # Regras de cálculo de custo
├── dados/                 # Planilhas de entrada (.xlsx)
└── README.md
```

---

## Tecnologias Utilizadas

* Python 3.x
* Streamlit
* Pandas
* Excel (fonte de dados)
* Git / GitHub

---

## Como Funciona

1. Os dados são carregados automaticamente da pasta `/dados`
2. O `dataframe.py` processa e estrutura os dados
3. O `consumo_agua.py` calcula consumo baseado em regras por máquina
4. O `gasto_financeiro.py` converte consumo em custo
5. O `app.py` exibe tudo em dashboard interativo

---

## Regras de Negócio

### Consumo de água (exemplo):

* Autoclave 1 e 2 → 200 L por ciclo
* Termodesinfectoras → 80 L por ciclo
* Outros → 30 L por ciclo

### Custo:

* Tarifa fixa aplicada: R$ 44,41 por m³

---

## Como Executar

### 1. Instalar dependências

```bash
pip install pandas streamlit openpyxl
```

### 2. Rodar o dashboard

```bash
streamlit run app.py
```

---

##  Exemplo de uso

* Filtrar por mês e máquina
* Visualizar consumo e custo em tempo real
* Comparar eficiência entre equipamentos
* Acompanhar evolução operacional

---

##  Objetivo do Projeto

Este sistema foi desenvolvido com foco em:

* Controle operacional hospitalar
* Análise de eficiência de equipamentos
* Redução de custos e desperdícios
* Apoio à tomada de decisão baseada em dados

---

## Autor

Projeto desenvolvido por **Daniel Pacheco**
