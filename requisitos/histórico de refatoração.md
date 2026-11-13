#Histórico de Refatoração

##REF01 - Substituição de variáveis individuais por dicionário

###Alteração:

Foi criado um dicionário chamado filme para armazenar os atributos de cada filme: nome, duração, gênero, sinopse, ano e nota.

Também foi criada uma lista chamada filmes, que recebe cada dicionário por meio do método append().

###Motivo:

A estrutura anterior utilizava variáveis individuais e permitia armazenar apenas um filme por vez.

###Resultado:

Os dados de cada filme passaram a ficar agrupados em um dicionário, enquanto a lista permite armazenar múltiplos filmes.

##REF02 - Adaptação da listagem de filmes

###Alteração:

A opção 2 do menu foi modificada para percorrer a lista filmes utilizando um laço for.

A exibição dos dados passou a acessar diretamente os atributos de cada dicionário.

###Motivo:

A lógica anterior utilizava variáveis individuais e não era compatível com a nova estrutura de armazenamento.

###Resultado:

O sistema passou a listar todos os filmes cadastrados, exibindo seus seis atributos individualmente.
