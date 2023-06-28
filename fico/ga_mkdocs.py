import numpy as np


def cal_pop_fitness(equation_inputs, pop, valor_investir, vencimento, pagamento):
    """Calcula o valor fitness de cada solução na população atual.

    Args:
        equation_inputs (np.ndarray): Entradas da equação.
        pop (np.ndarray): População atual.
        valor_investir (float): Valor a ser investido.
        vencimento (np.ndarray): Vetor de vencimento.
        pagamento (np.ndarray): Vetor de pagamentos.

    Returns:
        np.ndarray: Valores fitness de cada solução.
    """
    # Calcula o valor fitness para cada solução na população atual
    fitness = np.sum(pop * equation_inputs, axis=1)

    # Define as posições para cada tipo de investimento na população
    pos_rv = 564
    pos_im = 1068
    pos_rf = 1116
    pos_fx = 1128
    sol_per_pop = len(pop)

    # Calcula o limite de investimento para cada tipo de investimento na população
    lim_rv = np.empty((sol_per_pop, 1))
    for i in range(0, sol_per_pop):
        lim_rv[i] = sum(pop[i][0:pos_rv])

    lim_im = np.empty((sol_per_pop, 1))
    for i in range(0, sol_per_pop):
        lim_im[i] = sum(pop[i][pos_rv:pos_im])

    lim_rf = np.empty((sol_per_pop, 1))
    for i in range(0, sol_per_pop):
        lim_rf[i] = sum(pop[i][pos_im:pos_rf])

    lim_fx = np.empty((sol_per_pop, 1))
    for i in range(0, sol_per_pop):
        lim_fx[i] = sum(pop[i][pos_rf:pos_fx])

    # Calcula as penalidades para cada tipo de investimento na população
    pen_rf = np.empty((sol_per_pop, 1))
    pen_rv = np.empty((sol_per_pop, 1))
    pen_im = np.empty((sol_per_pop, 1))
    pen_fx = np.empty((sol_per_pop, 1))

    for i in range(0, sol_per_pop):
        pen_rf[i] = max(0, (lim_rf[i]) - valor_investir)
        pen_rv[i] = max(0, (lim_rv[i]) - valor_investir * 0.1)
        pen_im[i] = max(0, (lim_im[i]) - valor_investir * 0.2)
        pen_fx[i] = max(0, (lim_fx[i]) - valor_investir * 0.10)

    # Aplica as penalidades ao valor fitness
    for i in range(0, sol_per_pop):
        fitness[i] -= pen_rf[i]

    for i in range(0, sol_per_pop):
        fitness[i] -= pen_rv[i]

    for i in range(0, sol_per_pop):
        fitness[i] -= pen_im[i]

    for i in range(0, sol_per_pop):
        fitness[i] -= pen_fx[i]

    # Segunda restrição
    pen_total = np.empty((sol_per_pop, 1))

    for i in range(0, sol_per_pop):
        pen_total[i] = max(0, (sum(pop[i])) - valor_investir)

    for i in range(0, sol_per_pop):
        fitness[i] -= pen_total[i]

    # TERCEIRA RESTRIÇÃO
    fluxo_saida = np.empty((12, 1))

    num_weights = len(equation_inputs)
    for t in range(0, 12):
        fluxo_saida[t] = pagamento[t] * valor_investir

    rend_mes = np.zeros((sol_per_pop, 12))

    for t in range(0, 12):  # tempo
        for i in range(0, sol_per_pop):  # indivíduo
            for j in range(0, num_weights):  # genes
                if vencimento[j] == t:
                    rend_mes[i, t] += pop[i][j] * equation_inputs[j] + pop[i][j]

    pen_tempo = np.empty(sol_per_pop)

    for i in range(0, sol_per_pop):
        for t in range(0, 12):
            pen_tempo[i] = abs(rend_mes[i, t] - fluxo_saida[t])

    for i in range(0, sol_per_pop):
        fitness[i] -= pen_tempo[i]

    # Quarta restrição

    pen_div_rv = np.zeros((sol_per_pop, 1))
    for i in range(0, sol_per_pop):
        for j in range(0, pos_rv):
            pen_div_rv[i] += max(0, pop[i][j] - 0.00005 * valor_investir)

    for i in range(0, sol_per_pop):
        fitness[i] -= pen_div_rv[i]

    pen_div_im = np.zeros((sol_per_pop, 1))
    for i in range(0, sol_per_pop):
        for j in range(pos_rv, pos_im):
            pen_div_im[i] += max(0, pop[i][j] - 0.00005 * valor_investir)

    for i in range(0, sol_per_pop):
        fitness[i] -= pen_div_im[i]

    return fitness


def select_mating_pool(pop, fitness, num_parents):
    """Seleciona os melhores indivíduos da geração atual como pais para produzir a descendência da próxima geração.

    Args:
        pop (np.ndarray): População atual.
        fitness (np.ndarray): Valores fitness de cada solução.
        num_parents (int): Número de pais a serem selecionados.

    Returns:
        np.ndarray: Pais selecionados.
    """
    parents = np.empty((num_parents, pop.shape[1]))
    for parent_num in range(num_parents):
        # Encontra o índice do indivíduo com o maior valor fitness
        max_fitness_idx = np.where(fitness == np.max(fitness))
        max_fitness_idx = max_fitness_idx[0][0]
        # Seleciona o indivíduo como pai e o adiciona à lista de pais
        parents[parent_num, :] = pop[max_fitness_idx, :]
        # Define um valor muito baixo para o valor fitness do indivíduo selecionado, para não ser selecionado novamente
        fitness[max_fitness_idx] = -99999999999
    return parents


def crossover(parents, offspring_size):
    """Realiza o crossover entre os pais para gerar a descendência.

    Args:
        parents (np.ndarray): Pais selecionados.
        offspring_size (tuple): Tamanho da descendência.

    Returns:
        np.ndarray: Descendência gerada pelo crossover.
    """
    offspring = np.empty(offspring_size)
    # O ponto em que ocorre o crossover entre dois pais. Geralmente, é no centro.
    crossover_point = np.uint8(offspring_size[1] / 2)

    for k in range(offspring_size[0]):
        # Índice do primeiro pai para acasalar.
        parent1_idx = k % parents.shape[0]
        # Índice do segundo pai para acasalar.
        parent2_idx = (k + 1) % parents.shape[0]
        # A nova descendência terá metade de seus genes retirados do primeiro pai.
        offspring[k, 0:crossover_point] = parents[parent1_idx, 0:crossover_point]
        # A nova descendência terá a outra metade de seus genes retirados do segundo pai.
        offspring[k, crossover_point:] = parents[parent2_idx, crossover_point:]
    return offspring


def mutation(offspring_crossover, num_mutations=1):
    """Realiza a mutação na descendência.

    Args:
        offspring_crossover (np.ndarray): Descendência após o crossover.
        num_mutations (int): Número de mutações a serem realizadas.

    Returns:
        np.ndarray: Descendência após a mutação.
    """
    mutations_counter = np.uint8(offspring_crossover.shape[1] / num_mutations)
    # A mutação altera um número de genes definido pelo argumento num_mutations. As alterações são aleatórias.
    for idx in range(offspring_crossover.shape[0]):
        gene_idx = mutations_counter - 1
        for _mutation_num in range(num_mutations):
            # O valor aleatório a ser adicionado ao gene.
            random_value = np.random.uniform(-10.0, 10.0, 1)
            offspring_crossover[idx, gene_idx] = (
                offspring_crossover[idx, gene_idx] + random_value
            )
            gene_idx = gene_idx + mutations_counter
    return offspring_crossover
