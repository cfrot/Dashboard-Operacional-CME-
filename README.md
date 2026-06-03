# Dashboard Operacional CME

## Sobre o Projeto

Este projeto foi desenvolvido para monitorar indicadores operacionais da Central de Material e Esterilização (CME), permitindo analisar produtividade, consumo de água e custos operacionais das autoclaves ao longo do período analisado.

A aplicação foi construída utilizando Python, Pandas e Streamlit, proporcionando uma visualização interativa dos dados por meio de gráficos, indicadores e tabelas analíticas.

---

## Objetivo

Fornecer uma ferramenta de apoio à tomada de decisão operacional através do acompanhamento de:

* Quantidade de ciclos realizados por máquina
* Consumo estimado de água
* Custo operacional estimado
* Participação operacional de cada equipamento
* Evolução mensal da produtividade
* Comparação entre equipamentos

---

## Tecnologias Utilizadas

* Python 3.13
* Pandas
* Streamlit
* OpenPyXL

---

## Estrutura do Projeto

```text
Dashboard-Operacional-CME/
│
├── app.py
├── dataframe.py
├── consumo_agua.py
├── gasto_financeiro.py
├── requirements.txt
├── README.md
│
├── assets/
│   └── logo.png
│
└── dados/
    ├── janeiro.xlsx
    ├── fevereiro.xlsx
    └── marco.xlsx
```

---

## Funcionalidades

### Indicadores Operacionais

* Total de ciclos realizados
* Consumo total de água
* Custo operacional estimado
* Máquina com maior utilização

### Visualizações

* Ciclos por máquina
* Consumo de água por máquina
* Custos por máquina
* Evolução mensal dos ciclos

### Tabelas Analíticas

Resumo por máquina contendo:

* Ciclos
* Consumo (m³)
* Custo total
* Participação operacional (%)
* Consumo por ciclo
* Custo por ciclo

---

## Fonte dos Dados

Os dados são importados automaticamente de planilhas Excel (.xlsx) localizadas na pasta:

```text
dados/
```

Cada arquivo representa um mês de operação da CME.

---

## Instalação

Clone o repositório:

```bash
git clone https://github.com/cfrot/Dashboard-Operacional-CME-.git
```

Acesse a pasta do projeto:

```bash
cd Dashboard-Operacional-CME-
```

Instale as dependências:

```bash
py -m pip install -r requirements.txt
```

---

## Execução

Inicie a aplicação com:

```bash
py -m streamlit run app.py
```

Após a execução, acesse:

```text
http://localhost:8501
```

---

## Resultados Obtidos

O dashboard permite acompanhar os principais indicadores operacionais da CME de forma visual e intuitiva, auxiliando no monitoramento da produtividade dos equipamentos e na análise de custos operacionais relacionados ao consumo de água.

---

## Autor

Daniel Pacheco


