This part of the project documentation focuses on an **understanding-oriented**
approach. You'll get a chance to read about the background of the project, as well as
reasoning about how it was implemented.

# Contexto

Este projeto foi desenvolvido para a disciplina PO 245 - Aprendizado de Máquina em Finanças Quantitativas, ofertada no Programa de Pós Graduação em Pesquisa Operacional do Instituto Tecnológico de Aeronáutica e Universidade Federal de São Paulo no primeiro semestre de 2023.

O projeto surgiu da identificação de um problema recorrente no mercado financeiro, especificamente no setor segurador: como realizar a gestão de ativos e passivos (também conhecido como *Asset-Liability Management - ALM*) da melhor maneira, atendendo às restrições existentes e ainda obtendo a melhor rentabilidade possível?

Dado o problema, artigos que analisam este problema foram considerados, inclusive no cenário internacional. Tais artigos propõem técnicas alternativas às que são utilizadas hoje, aplicando Algoritmos Genéticos para a construção da política ótima de investimentos e realizando avaliações sobre o resultado obtido.

O objetivo deste projeto é elaborar, através da aplicação de Algoritmo Genético, uma política ótima de investimentos considerando as restrições de uma seguradora, restrições tanto regulatórias quanto operacionais.

# Solução

A solução proposta para o problema de ALM mencionado anteriormente foi desenvolver a política de investimentos através da aplicação de Algoritmo Genético, considerando dados reais para ativos, como, por exemplo, cotações do mercado de valores mobiliários e ainda características reais do setor provenientes da seguradora Azul Companhia de Seguros Gerais S.A., obtidas das demonstrações financeiras oficiais publicadas.

A solução proposta foi elaborada com o intuito de ser utilizada como uma biblioteca por interessados no assunto. A biblioteca contém funções definidas internamente que serão utilizadas no decorrer de sua aplicação, além de seleção de informações a serem consideradas.

A solução foi elaborada para ser flexível podendo ser aplicada a dados alternativos aos considerados no código. Vale ressaltar que algumas premissas foram adotadas, premissas estas que simplificam o problema para que possa ser analisado e estudado aqui neste projeto.
