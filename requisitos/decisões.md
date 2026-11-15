# Decisões do Projeto

## DEC01 - Tipo de dado para o nome

O campo "Nome" foi definido como `string`, pois o nome de um filme é formado por letras, palavras e pode conter espaços.

## DEC02 - Tipo de dado para a duração

O campo "Duração" foi definido como `int`, pois a duração do filme será informada em minutos e será representada por um número inteiro.

## DEC03 - Tipo de dado para o gênero

O campo "Gênero" foi definido como `string`, pois o gênero de um filme é representado por palavras, como "Ação", "Comédia" ou "Drama".

## DEC04 - Tipo de dado para a sinopse

O campo "Sinopse" foi definido como `string`, pois a sinopse contém um texto que descreve o filme.

## DEC05 - Tipo de dado para o ano

O campo "Ano" foi definido como `int`, pois o ano de lançamento é representado por um número inteiro.

## DEC06 - Tipo de dado para a nota

O campo "Nota" foi definido como `float`, pois a avaliação de um filme pode possuir valores decimais, como 8.5 ou 9.7.

## DEC07 - Validação da nota

Foi definido que a nota deve estar entre 0 e 10, pois essa é a escala utilizada para avaliar os filmes no sistema.

## DEC08 - Validação do nome

Foi definido que o nome do filme não pode ficar vazio, pois todo filme cadastrado precisa possuir um nome para ser identificado.

## DEC09 - Validação da duração

Foi definido que a duração deve ser maior que 0, pois um filme precisa possuir uma duração válida para ser cadastrado.

## DEC10 - Classificação do lançamento

Foi definido que o sistema deve classificar o filme de acordo com o ano de lançamento. Filmes com ano menor ou igual ao ano atual serão classificados como "Já lançado", enquanto filmes com ano maior que o ano atual serão classificados como "Vai ser lançado".

## DEC11 - Execução pelo terminal

Foi definido que o sistema será executado pelo terminal, pois o objetivo do projeto é desenvolver uma aplicação simples, adequada ao nível atual de aprendizado e aos conteúdos da disciplina.

## DEC12 - Desenvolvimento em Python

Foi escolhida a linguagem Python para o desenvolvimento do sistema, por ser a linguagem utilizada na disciplina de Algoritmos e Programação e por permitir a implementação do CRUD de forma simples.

## DEC13 - Funcionamento sem internet

Foi definido que o sistema não dependerá de conexão com a internet, pois todas as operações do CRUD serão realizadas localmente.

# Decisões da refatoração

# 13/11/2026:

## DEC 14 - Estrutura de armazenamento dos dados

### Decisão:

Foi definida a utilização de listas e dicionários, porque o código atual só usa variáveis para guardar seus dados. O dicionário permitirá organizar os atributos de cada filme em uma única estrutura, enquanto a lista permitirá armazenar múltiplos filmes.

### Justificativa técnica:

A utilização de uma lista de dicionários permite agrupar os atributos relacionados a cada filme e armazenar múltiplos registros em uma única estrutura. O dicionário organiza as informações por meio de pares de chave e valor, enquanto a lista possibilita adicionar, percorrer e remover registros dinamicamente.

### Consequência:

O sistema poderá armazenar vários filmes em uma única estrutura, facilitando as operações de cadastro, listagem, atualização e exclusão. A remoção de um filme também fará com que os índices dos elementos seguintes sejam reorganizados automaticamente.

## DEC15 — Utilização de laço de repetição na listagem

### Decisão:

Foi definido o uso da estrutura de repetição `for` na opção 2 do CRUD para percorrer a lista `filmes` e acessar individualmente cada dicionário armazenado.

### Justificativa técnica: 

como a quantidade de filmes cadastrados pode variar, o laço `for` permite percorrer todos os elementos da lista sem precisar criar instruções específicas para cada registro.

### Consequência: 
a listagem passa a exibir todos os filmes cadastrados, acompanhando automaticamente a quantidade de elementos presentes na lista.

## DEC16 — Seleção de filmes por índice

### Decisão:

Foi definido o uso dos índices da lista `filmes` para permitir que o usuário selecione individualmente qual filme deseja atualizar ou excluir. A exibição utiliza uma numeração iniciada em 1, enquanto o código converte a escolha para o índice correspondente da lista, subtraindo 1.

### Justificativa técnica:

As listas em Python utilizam índices que começam em 0, mas a numeração iniciada em 1 facilita a identificação dos filmes pelo usuário. A conversão permite manter uma interação mais intuitiva sem comprometer o acesso correto aos elementos.

### Consequência:

O usuário poderá selecionar um filme específico para realizar operações de atualização e exclusão, sem precisar manipular diretamente os dados da lista.

## DEC17 — Atualização dos dados diretamente no dicionário

### Decisão:

Foi definido que a atualização dos dados de um filme será realizada diretamente no dicionário correspondente ao registro selecionado, modificando os valores associados às suas chaves.

### Justificativa técnica:

Como cada filme é representado por um dicionário, seus atributos podem ser acessados e modificados por meio de suas chaves, como `nome`, `duracao`, `genero`, `sinopse`, `ano` e `nota`. Dessa forma, não é necessário criar outro registro ou reconstruir toda a lista para alterar uma informação.

### Consequência:

O sistema poderá modificar os dados de um filme específico, mantendo sua posição na lista e preservando os demais registros.

## DEC18 — Exclusão de registros utilizando `pop()`

### Decisão:

Foi definido o uso do método `pop()` para excluir um filme selecionado pelo usuário, utilizando o índice correspondente ao registro na lista `filmes`.

### Justificativa técnica:

Durante a implementação, foi necessário compreender a diferença entre os métodos `remove()` e `pop()`. Enquanto `remove()` procura e remove um elemento pelo seu valor, `pop()` permite remover um elemento a partir de sua posição na lista. Como a seleção do filme é feita por índice, `pop()` atende melhor à necessidade da operação.

### Consequência:

O sistema poderá excluir um filme específico da lista. Após a remoção, os elementos seguintes terão seus índices reorganizados automaticamente, mantendo a estrutura da lista atualizada.
