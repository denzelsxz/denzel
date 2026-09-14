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
