# LOGBOOK — CRUD NETFLIX

# PARTE 1 — CICLOS DE DESENVOLVIMENTO

## Ciclo 1 — Planejamento e levantamento de requisitos

Nesta etapa, defini as informações que seriam armazenadas para cada filme: nome, duração, gênero, sinopse, ano de lançamento e nota.

Também determinei os tipos de dados de cada atributo e estabeleci algumas regras para o cadastro, como impedir nomes vazios, exigir duração maior que zero e limitar a nota entre 0 e 10.

Defini Python como linguagem de programação e o terminal como ambiente de execução. O projeto foi planejado para funcionar sem conexão com a internet.

**Documentação relacionada:** `requisitos.md` e `decisoes.md`.

## Ciclo 2 — Primeira implementação do CRUD

Desenvolvi a primeira versão do CRUD utilizando variáveis individuais para armazenar os dados de um filme.

Implementei um menu interativo com opções para cadastrar, listar, atualizar e excluir informações. Para controlar a execução do programa, utilizei estruturas condicionais e de repetição.

Durante essa etapa, identifiquei uma limitação na estrutura escolhida: como os atributos estavam armazenados em variáveis individuais, o programa permitia trabalhar somente com um filme por vez.

Também identifiquei que algumas validações definidas no planejamento ainda não estavam implementadas no código.

Não realizei os registros no Logbook durante esse ciclo por uma falha minha na organização e no acompanhamento da documentação. Reconstruí posteriormente as atividades com base no código e nos arquivos disponíveis.

## Ciclo 3 — Refatoração da estrutura de armazenamento

**Data: 13/11/2026**

Iniciei a refatoração do CRUD para permitir o armazenamento de vários filmes.

Primeiramente, criei uma lista chamada `filmes`, que passou a armazenar os registros. Em seguida, organizei os atributos de cada filme em um dicionário, utilizando os nomes dos atributos como chaves e os respectivos valores como dados.

Utilizei o método `append()` para adicionar cada novo dicionário à lista.

Depois, adaptei a opção de listagem para percorrer a lista com um laço `for` e apresentar individualmente os atributos de cada filme.

Durante a implementação, cometi um erro ao utilizar uma variável diferente daquela que representava o elemento percorrido pelo laço. Corrigi o problema utilizando a variável correta para acessar as chaves do dicionário.

Inicialmente, também utilizei `print(filmes)` para exibir os registros. Embora essa instrução apresentasse os dados, decidi exibir cada atributo separadamente para tornar a saída mais organizada e compreensível.

Testei o cadastro de mais de um filme e confirmei que a listagem apresentava os registros corretamente.

**Resultado:** o cadastro e a listagem passaram a utilizar a nova estrutura de lista de dicionários. As opções de atualização e exclusão ainda precisam ser adaptadas.

**Documentação relacionada:** DEC14 em `decisoes.md` e REF01 e REF02 em `historico-refatoracao.md`.

---

# PARTE 2 — CAMPO 1: ENTRADA

## O que acredito saber

Tenho conhecimentos iniciais de lógica de programação e Python, adquiridos durante as aulas e aplicados no desenvolvimento da primeira versão do CRUD.

### 1. Fundamentos de lógica de programação

Acredito compreender o conceito de algoritmo como uma sequência de instruções organizadas para resolver determinado problema.

Conheço a estrutura IPO (Entrada, Processamento e Saída) e consigo identificar esses elementos na construção de um algoritmo.

Também conheço as representações de algoritmos por meio de linguagem natural, pseudocódigo e fluxogramas, compreendendo a relação entre essas etapas e sua implementação em uma linguagem de programação.

Tenho conhecimento inicial sobre programação procedural e sobre a organização de instruções em uma sequência lógica.

### 2. Variáveis e tipos de dados

Sei declarar e utilizar variáveis para armazenar informações durante a execução de um programa.

Conheço os principais tipos de dados utilizados em Python:

- `int`: números inteiros;
- `float`: números decimais;
- `str`: textos;
- `bool`: valores booleanos (`True` e `False`).

Também sei realizar conversões entre tipos de dados utilizando recursos como `int()`, `float()` e `str()`.

Compreendo a diferença entre o operador de atribuição (`=`) e o operador de comparação (`==`).

### 3. Operadores

Conheço e consigo utilizar operadores aritméticos, relacionais e lógicos.

Entre os operadores estudados estão:

- Aritméticos: `+`, `-`, `*`, `/`, `//`, `%` e `**`;
- Relacionais: `==`, `!=`, `>`, `<`, `>=` e `<=`;
- Lógicos: `and`, `or` e `not`.

Também sei utilizar operadores de atribuição composta, como `+=`, e compreendo o uso do operador módulo (`%`) em operações matemáticas.

### 4. Estruturas condicionais

Sei utilizar as estruturas `if`, `elif` e `else` para controlar o fluxo de execução de um programa de acordo com determinadas condições.

Consigo combinar condições utilizando operadores lógicos e aplicar estruturas condicionais em situações como validação de dados e seleção de opções de um menu.

### 5. Estruturas de repetição

Conheço e consigo utilizar as estruturas `while` e `for`.

Compreendo que o `while` executa instruções enquanto uma condição for verdadeira e que o `for` permite percorrer sequências de elementos.

Também conheço o uso de `range()` para gerar sequências numéricas e as instruções `break` e `continue` para controlar a execução dos laços.

Já apliquei essas estruturas no CRUD para manter o menu em execução e percorrer os registros armazenados.

### 6. Estruturas de dados

Tenho conhecimento inicial sobre listas e dicionários em Python.

**Listas:**
- Sei criar listas e armazenar vários elementos;
- Sei acessar elementos utilizando índices;
- Compreendo que os índices começam em zero;
- Sei utilizar o método `append()` para adicionar elementos;
- Consigo percorrer listas utilizando estruturas de repetição;
- Sei utilizar `len()` para obter a quantidade de elementos.

**Dicionários:**
- Sei criar dicionários utilizando pares de chave e valor;
- Sei acessar valores por meio de suas chaves;
- Compreendo que um dicionário permite organizar informações relacionadas a um mesmo registro;
- Sei que diferentes tipos de dados podem ser armazenados em um dicionário.

Já comecei a aplicar esses conhecimentos no CRUD, utilizando uma lista para armazenar vários dicionários, cada um representando um filme.

### 7. Funções

Tenho conhecimento básico sobre a criação e utilização de funções em Python.

Sei que uma função pode ser definida utilizando `def`, receber parâmetros e executar um conjunto de instruções.

Também compreendo a utilização de `return` para devolver um resultado ao ponto em que a função foi chamada e a diferença entre retornar um valor e apenas exibi-lo com `print()`.

Apesar de conhecer esses conceitos, ainda preciso praticar sua aplicação na organização e divisão de programas em partes menores.

### 8. Funções nativas e métodos

Conheço e já utilizei algumas funções nativas e métodos de Python, como:

- `print()`: exibir informações;
- `input()`: receber dados do usuário;
- `len()`: obter a quantidade de elementos;
- `append()`: adicionar elementos a uma lista.

Consigo aplicar esses recursos em situações simples, mas ainda preciso ampliar meu conhecimento sobre os métodos disponíveis para listas e dicionários.

### 9. Aplicação prática dos conhecimentos

Já apliquei parte desses conhecimentos no desenvolvimento de um CRUD em Python.

Na primeira versão, implementei um menu interativo com operações de cadastro, listagem, atualização e exclusão.

Na refatoração, comecei a substituir variáveis individuais por uma estrutura composta por lista e dicionários, permitindo armazenar vários filmes.

Acredito conseguir desenvolver programas simples utilizando variáveis, operadores, condicionais, laços de repetição e estruturas de dados básicas, embora ainda precise consolidar esses conhecimentos por meio da prática.

## O que ainda preciso compreender melhor

- Combinar listas e dicionários para organizar conjuntos de registros;
- Percorrer uma lista e localizar um registro específico;
- Atualizar valores armazenados em um dicionário;
- Remover elementos de uma lista;
- Adaptar todas as operações do CRUD à nova estrutura de armazenamento;
- Aplicar validações de entrada de maneira consistente;
- Utilizar funções para dividir o programa em partes menores e organizadas;
- Compreender melhor como utilizar parâmetros e retornos na construção de funções.

## Hipótese inicial

Acredito que a utilização de uma lista contendo dicionários seja uma estrutura adequada para armazenar vários filmes.

Cada dicionário representa um filme e contém seus atributos. A lista reúne todos os filmes cadastrados.

Essa organização deve permitir que as operações de cadastro, listagem, atualização e exclusão trabalhem com vários registros, sem depender de variáveis individuais para cada filme.

---

# PARTE 3 — CAMPO 2: APROFUNDAMENTO

## Objeto de conhecimento

Estruturas de dados em Python, principalmente listas e dicionários, e sua aplicação na organização de registros.

## Justificativa técnica

A estrutura anterior utilizava variáveis individuais para armazenar os atributos de um único filme. Essa organização limitava a capacidade do programa.

A utilização de uma lista de dicionários permite agrupar os atributos de cada filme e armazenar vários registros em uma única estrutura.

## Referência de estudo

Documentação oficial do Python — Estruturas de dados:

https://docs.python.org/3/tutorial/datastructures.html


## Análise crítica do auxílio da IA

Durante a refatoração, utilizei a IA como apoio para esclarecer dúvidas e avaliar alternativas de implementação.

Aceitei a utilização de uma lista de dicionários porque a estrutura atende à necessidade de armazenar vários filmes e organizar seus atributos.

Também aceitei a utilização de um laço `for` para percorrer os registros e apresentar os dados individualmente.

Questionei a utilização de `print(filmes)` como forma de listagem. Embora a instrução funcionasse, considerei que apresentar cada atributo separadamente tornaria a saída mais organizada.

Também procurei compreender onde documentar as alterações realizadas, diferenciando as decisões técnicas do histórico de mudanças no código e dos registros pessoais de aprendizagem.

**Observação:**
Este logbook ainda está em desenvolvimento, logo o campo 2, bem como os ciclos, ainda não estão completos na data desta alteração (13/11/2026)
