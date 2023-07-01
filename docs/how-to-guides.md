Esta parte da documentação do projeto centra-se numa
**abordagem orientada para os problemas**. Irá lidar com tarefas
tarefas comuns que você pode ter, com a ajuda do código
fornecido neste projeto.

## How To: Atualizar a curva de pagamentos?

No módulo principal *alm_insurance.py*, insira os novos valores na variável **pagamento** para os 12 meses considerados. Caso a opção seja a geração estocástica de valores, modifique também esta variável.

    # alm_insurance.py
    pagamento = [0.29, 0.20, 0.12, 0.07, 0.06, 0.05, 0.07, 0.06, 0.04, 0.01, 0.02, 0.01]

## How To: Atualizar os dados dos ativos?

Ainda no mesmo módulo principal *alm_insurance.py*, altere o arquivo csv *assets_inputs.csv* contendo as novas informações de nome de ativo, vencimento e rentabilidade.

    # alm_insurance.py

    dados_ativos = pd.read_csv("assets_inputs.csv")

    vencimento = list(dados_ativos["Vencimento"])

    equation_inputs = list(dados_ativos["Rentabilidade"])

## How to: Alterar o valor disponível a ser investido?

Seguindo no módulo principal *alm_insurance.py*, altere o valor da variável *valor_investir* para o valor desejado.

    # alm_insurance.py

    valor_investir = 1461073

## How to: Alterar os parâmetros do Algoritmo Genético?

considerando o módulo *alm_insurance.py*, altere os parâmetros:

1. sol_per_pop: caso queria alterar a quantidade de soluções por população;
1. num_parents_mating: caso queia alterar a quantidade de pais selecionados;
1. n_mut: a quantidade de mutações definida;
1. num_generations: a quantidade máxima de gerações;
1. valor_max: o valor máximo a ser alocado em cada alternativa de investimentos.

        # alm_insurance.py

        sol_per_pop = 20
        num_parents_mating = 8
        n_mut = 20
        num_generations = 100
        valor_max = 4000000
