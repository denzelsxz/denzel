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

**Resultado:** o cadastro e a listagem passaram a utilizar a nova estrutura de lista de dicionários. Com isso, a estrutura de armazenamento deixou de depender de variáveis individuais para representar apenas um filme. As operações de atualização e exclusão foram tratadas em um ciclo separado.

**Documentação relacionada:** DEC14 em `decisoes.md` e REF01 e REF02 em `historico-refatoracao.md`.

## Ciclo 4 — Adaptação das operações de atualização e exclusão

**Data: 15/11/2026**

Após modificar a estrutura de armazenamento, adaptei as operações de atualização e exclusão para que também trabalhassem com a lista de dicionários.

Na opção de atualização, passei a apresentar os filmes cadastrados em uma lista numerada. Para isso, utilizei um laço `for` com `range(len(filmes))`, exibindo `i + 1` ao usuário para que a seleção começasse em 1, embora os índices da lista comecem em 0.

Depois que o usuário escolhe um filme, utilizo o número informado para acessar o registro correspondente na lista. A atualização é feita diretamente nas chaves do dicionário selecionado, substituindo os valores dos atributos escolhidos. Dessa forma, as alterações permanecem no próprio registro armazenado na lista.

Na opção de exclusão, também apresento os filmes cadastrados de forma numerada e solicito que o usuário selecione um deles. Antes de excluir, o programa mostra o filme escolhido e pede uma confirmação. Quando a exclusão é confirmada, utilizo o método `pop()` com o índice correspondente para remover o dicionário da lista. Caso a operação seja cancelada, o registro é mantido.

Essa adaptação exigiu compreender melhor a relação entre os índices da lista e os registros armazenados, além de como acessar e modificar os valores de um dicionário por meio de suas chaves.

**Resultado:** as operações de cadastro, listagem, atualização e exclusão passaram a utilizar a estrutura de lista de dicionários, permitindo que o CRUD trabalhe com vários filmes. A atualização modifica diretamente o registro selecionado, enquanto a exclusão remove o elemento correspondente da lista.

**Testes realizados:** após a implementação, executei testes das opções de atualização e exclusão para verificar o funcionamento das duas operações. O registro confirma que ambas foram testadas; os cenários específicos e os resultados individuais não foram detalhados aqui.

**Documentação relacionada:** DEC14 em `decisoes.md` e registro das alterações REF03 e REF04 em `historico-refatoracao.md`, caso essas referências sejam adicionadas ao histórico.

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

## Objetos de conhecimento aprofundados

O aprofundamento esteve relacionado principalmente aos conteúdos mobilizados nos ciclos 3 e 4 do desenvolvimento do CRUD: estruturas de dados (listas e dicionários), iteração com `for`, acesso a elementos por índices, acesso e alteração de valores por chaves, métodos de listas e adaptação de operações já existentes a uma nova organização dos dados.

A mudança não envolveu apenas aprender um método isolado. Foi necessário compreender como a nova estrutura de armazenamento afetava o funcionamento do programa como um todo e como cada operação do CRUD deveria interagir com ela.

## Problema que motivou o aprofundamento

Na primeira versão do CRUD, os atributos do filme eram armazenados em variáveis individuais. Essa organização permitia trabalhar com um único filme por vez. Ao perceber essa limitação, precisei pensar em uma forma de reunir os dados de cada filme e, ao mesmo tempo, permitir que o programa armazenasse vários registros.

A partir desse problema, o trabalho foi dividido em duas etapas relacionadas: no ciclo 3, concentrei-me em mudar a estrutura de armazenamento e adaptar o cadastro e a listagem; no ciclo 4, adaptei a atualização e a exclusão para que também funcionassem com a nova estrutura.

## Aprofundamento realizado no Ciclo 3 — Estrutura de armazenamento, cadastro e listagem

### 1. Organização dos dados com lista e dicionários

No ciclo 3, aprofundei a compreensão de como combinar duas estruturas de dados. Passei a utilizar uma lista chamada `filmes` para reunir os registros e um dicionário para organizar os atributos de cada filme.

Essa organização foi escolhida porque cada filme possui um conjunto de informações relacionadas — nome, duração, gênero, sinopse, ano e nota. O dicionário mantém esses atributos agrupados por meio de chaves, enquanto a lista permite armazenar vários desses registros.

Utilizei o método `append()` para inserir cada novo dicionário na lista. Com isso, o cadastro deixou de depender de um conjunto fixo de variáveis individuais e passou a adicionar novos registros à mesma coleção.

### 2. Percorrer a lista e apresentar os filmes

Também precisei adaptar a listagem. Em vez de apresentar um único conjunto de variáveis, passei a percorrer a lista com um laço `for`, acessando os atributos de cada dicionário por suas chaves.

Durante essa implementação, cometi um erro ao utilizar um nome de variável diferente daquele definido no próprio laço. Como consequência, a referência utilizada para acessar os dados não correspondia ao elemento que estava sendo percorrido. Revisei o trecho e corrigi o identificador, compreendendo que a variável do `for` representa, a cada repetição, o elemento atual da lista.

Outro ponto que avaliei foi a forma de exibir os registros. Inicialmente, utilizei `print(filmes)`, que mostrava o conteúdo da lista, mas não apresentava os dados da maneira mais organizada para o usuário. Optei por percorrer os dicionários e imprimir cada atributo separadamente. Aceitei essa organização porque facilita a leitura das informações de cada filme, em vez de apresentar diretamente a estrutura completa da lista.


## Aprofundamento realizado no Ciclo 4 — Atualização e exclusão dos registros

A mudança realizada no ciclo 3 exigiu que as operações restantes também fossem adaptadas. No ciclo 4, o desafio foi localizar um filme específico dentro da lista e realizar uma alteração ou remoção sem afetar os demais registros.

### 1. Selecionar e atualizar um filme — opção 3

Na atualização, passei a apresentar os filmes cadastrados em uma lista numerada. Para gerar essa numeração, utilizei `range(len(filmes))` e mostrei `i + 1` ao usuário.

Esse ponto exigiu atenção porque os índices de uma lista em Python começam em zero, enquanto a numeração apresentada ao usuário começa em um. Portanto, para acessar o registro correspondente à opção escolhida, é necessário subtrair um do número informado. Depois de localizar o dicionário, a alteração é feita diretamente em uma de suas chaves, como `filme["nome"]` ou `filme["nota"]`.

Aceitei essa abordagem porque permite selecionar um registro específico e modificar somente o atributo escolhido. Também compreendi que, como a variável `filme` referencia o dicionário que está armazenado na lista, a alteração feita nele permanece no próprio registro, sem precisar adicionar o filme novamente com `append()`.

### 2. Selecionar e excluir um filme — opção 4

Na exclusão, utilizei uma lógica semelhante para apresentar os filmes numerados e permitir que o usuário escolhesse qual registro remover. Antes da remoção, o programa mostra o filme selecionado e solicita uma confirmação.

Durante o desenvolvimento, questionei se poderia utilizar `filmes.remove([1])` para excluir o segundo elemento. A discussão ajudou a esclarecer que `remove()` procura um elemento pelo valor informado, enquanto `pop()` remove o elemento localizado em determinada posição. Como a necessidade do CRUD era excluir o filme escolhido pelo índice, a utilização de `pop(indice - 1)` mostrou-se mais adequada.

Também considerei o que acontece com os índices quando um elemento é removido do meio da lista. Compreendi que os elementos seguintes passam a ocupar posições anteriores. Portanto, o índice representa a posição atual do filme na lista, e não um identificador permanente daquele registro.

Mantive a confirmação antes da exclusão porque ela oferece ao usuário a possibilidade de cancelar a operação. Se a confirmação não for dada, o registro permanece na lista.

## Referência de estudo

Utilizei como referência a documentação oficial do Python sobre estruturas de dados, especialmente os conteúdos relacionados a listas, métodos de listas e formas de percorrer sequências:

Documentação oficial do Python — Estruturas de dados:
https://docs.python.org/3/tutorial/datastructures.html

A documentação serviu como material de consulta para compreender os recursos utilizados na implementação. Relacionei esses conceitos às necessidades concretas do CRUD, em vez de estudá-los apenas de forma isolada.

## Síntese do aprofundamento

Os ciclos 3 e 4 ampliaram minha compreensão sobre como as estruturas de dados influenciam a organização e o funcionamento de um programa. No ciclo 3, compreendi como agrupar os atributos de cada filme em um dicionário, armazenar vários registros em uma lista e percorrer essa coleção para apresentar os dados. No ciclo 4, apliquei essa estrutura às operações de atualização e exclusão, trabalhando com índices para localizar os registros e com chaves para modificar seus atributos.

Além de implementar as mudanças, precisei avaliar alternativas, questionar o comportamento de métodos e corrigir erros durante o processo. O uso da IA ocorreu como apoio à revisão e à discussão técnica, enquanto a análise do problema, a escrita do código e a decisão de incorporar as alterações permaneceram sob minha responsabilidade.
