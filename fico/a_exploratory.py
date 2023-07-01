"""Este é um módulo módulo auxiliar no qual a análise exploratória é realizada."""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def analyze_investments():
    """Realiza análises de investimentos em diferentes tipos de ativos."""
    # Importa os dados relativos aos investimentos sujeitos à variação cambial
    dados_fx = pd.read_csv("fx.csv")

    # Converte a informação de data para o formato data do python
    dados_fx["Data"] = pd.to_datetime(dados_fx["Data"])

    # Define a data como índice da base de dados
    dados_fx = dados_fx.set_index("Data")

    # Importa os dados relativos aos investimentos de renda variável
    dados_rv = pd.read_csv("rv.csv")

    # Importa os dados relativos aos investimentos de renda fixa
    dados_imob = pd.read_csv("imob.csv")

    analyze_fx(dados_fx)
    analyze_rv(dados_rv)
    analyze_imob(dados_imob)


def analyze_fx(dados_fx):
    """Realiza análise para investimentos sujeitos à variação cambial.

    Args:
        dados_fx (pandas.DataFrame): Dados relativos aos investimentos sujeitos à
        variação cambial.
    """
    # Plotar a série temporal
    plt.plot(dados_fx)
    plt.xlabel("Data")
    plt.ylabel("Cotação")
    plt.title("Série Temporal - BRL/USD")
    plt.xticks(rotation="vertical")
    plt.show()

    # Verificar estatísticas descritivas das variáveis numéricas
    print("\nEstatísticas descritivas:")
    print(dados_fx.describe())


def analyze_rv(dados_rv):
    """Realiza análise para investimentos de renda variável.

    Args:
        dados_rv (pandas.DataFrame): Dados de investimentos de renda variável.
    """
    # Configurar DataFrame
    dados = pd.DataFrame(dados_rv)

    # Configurar DataFrame com 'Ativos' como índice
    dados = dados.set_index("Empresa")

    # Plotar gráfico de barras agrupadas
    dados.plot(kind="bar")
    plt.xlabel("Ativos")
    plt.ylabel("Rentabilidade")
    plt.title("Rentabilidade dos Ativos por Período")
    plt.legend(loc="best")
    plt.xticks(np.arange(len(dados.index)), dados.index, rotation="vertical")
    plt.show()


def analyze_imob(dados_imob):
    """Realiza análise para investimentos de renda fixa.

    Args:
        dados_imob (pandas.DataFrame): Dados relativos aos investimentos de renda fixa.
    """
    # Configurar DataFrame
    dados_2 = pd.DataFrame(dados_imob)

    # Configurar DataFrame com 'Ativos' como índice
    dados_2 = dados_2.set_index("Empresa")

    # Plotar gráfico de barras agrupadas
    dados_2.plot(kind="bar")
    plt.xlabel("Ativos")
    plt.ylabel("Rentabilidade")
    plt.title("Rentabilidade dos Ativos por Período")
    plt.legend(loc="best")
    plt.xticks(np.arange(len(dados_2.index)), dados_2.index, rotation="vertical")
    plt.show()


analyze_investments()
