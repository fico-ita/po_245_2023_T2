"""Este é o módulo principal no qual o algoritmo genético é processado."""

import itertools
import subprocess

import ga_mkdocs
import numpy as np
import pandas as pd
import plotly.graph_objects as go


def main():
    """Função principal para executar o algoritmo genético."""
    # Chama a execução de outro programa
    subprocess.call(["python", "a_exploratory.py"])

    # Geração discreta de um fluxo de pagamentos (gerado aleatoriamente)
    pagamento = [0.29, 0.20, 0.12, 0.07, 0.06, 0.05, 0.07, 0.06, 0.04, 0.01, 0.02, 0.01]

    # Lê os dados dos ativos disponíveis a partir de um arquivo CSV
    dados_ativos = pd.read_csv("assets_inputs.csv")

    # Vencimentos dos ativos disponíveis
    vencimento = list(dados_ativos["Vencimento"])

    # Dados provenientes do balanço patrimonial da Azul Cia Gerais de Seguros S.A.
    # publicado no veículo Monitor Mercantil
    valor_investir = 1461073

    # Rentabilidade dos ativos disponíveis
    equation_inputs = list(dados_ativos["Rentabilidade"])

    num_weights = len(equation_inputs)

    sol_per_pop = 20
    num_parents_mating = 8
    n_mut = 20
    num_generations = 100
    valor_max = 4000000

    pop_size = (sol_per_pop, num_weights)

    # Gera uma população inicial aleatória
    pop = np.random.default_rng().integers(low=0, high=valor_max, size=pop_size)

    best_outputs = []
    aux_fit = []
    bf_position = []

    for generation in range(1, num_generations + 1):
        print("Generation:", generation)

        # Calcula a aptidão de cada cromossomo na população
        fitness = ga_mkdocs.cal_pop_fitness(
            equation_inputs,
            pop,
            valor_investir,
            vencimento,
            pagamento,
        )

        aux = np.max(np.sum(pop * equation_inputs, axis=1))
        best_outputs.append(aux)

        fitness_gen = np.max(
            ga_mkdocs.cal_pop_fitness(
                equation_inputs,
                pop,
                valor_investir,
                vencimento,
                pagamento,
            ),
        )
        aux_fit.append(fitness_gen)

        # Seleciona os pais para a reprodução
        parents = ga_mkdocs.select_mating_pool(pop, fitness, num_parents_mating)

        aux2 = (pop_size[0] - parents.shape[0], num_weights)
        # Realiza o cruzamento dos pais para gerar descendentes
        offspring_crossover = ga_mkdocs.crossover(parents, offspring_size=aux2)

        # Realiza a mutação nos descendentes gerados
        offspring_mutation = ga_mkdocs.mutation(
            offspring_crossover,
            num_mutations=n_mut,
        )

        # Substitui parte da população atual pelos pais selecionados e descendentes
        # mutados
        pop[0 : parents.shape[0], :] = parents
        pop[parents.shape[0] :, :] = offspring_mutation

        best_fit_idx_gen = np.where(fitness == np.max(fitness))
        bf_position.append(best_fit_idx_gen)

        np.where(np.max(aux_fit))

        estrat_aloc = pop[best_fit_idx_gen, :]

    valor_resgate = np.zeros((12, 1))
    for t, j in itertools.product(range(12), range(num_weights)):
        if vencimento[j] == t:
            valor_resgate[t] += (
                estrat_aloc[0][0][j] * equation_inputs[j] + estrat_aloc[0][0][j]
            )

    # Plotar os resultados
    x = np.linspace(0, num_generations, num_generations)
    _extracted_from_main_109(x, best_outputs, "Best Outputs", "Best Outputs")
    _extracted_from_main_109(x, aux_fit, "Aux Fit", "Fitness")


# TODO Rename this here and in `main`
def _extracted_from_main_109(x, y, title, yaxis_title):
    result = go.Figure()

    result.add_trace(go.Scatter(x=x, y=y, mode="lines"))

    result.update_layout(title=title, xaxis_title="Generation", yaxis_title=yaxis_title)
    result.show()

    return result


if __name__ == "__main__":
    main()
