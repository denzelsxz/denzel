# Histórico de Refatoração

# 13/11/2026:

## REF01 - Substituição de variáveis individuais por dicionário

### Alteração:

Foi criado um dicionário chamado filme para armazenar os atributos de cada filme: nome, duração, gênero, sinopse, ano e nota.

Também foi criada uma lista chamada filmes, que recebe cada dicionário por meio do método append().

### Motivo:

A estrutura anterior utilizava variáveis individuais e permitia armazenar apenas um filme por vez.

### Resultado:

Os dados de cada filme passaram a ficar agrupados em um dicionário, enquanto a lista permite armazenar múltiplos filmes.

## REF02 - Adaptação da listagem de filmes

### Alteração:

A opção 2 do menu foi modificada para percorrer a lista filmes utilizando um laço for.

A exibição dos dados passou a acessar diretamente os atributos de cada dicionário.

### Motivo:

A lógica anterior utilizava variáveis individuais e não era compatível com a nova estrutura de armazenamento.

### Resultado:

O sistema passou a listar todos os filmes cadastrados, exibindo seus seis atributos individualmente.

# 15/11/2026:

## REF03 - Implementação da atualização de filmes

### Alteração:

A opção 3 do menu foi adaptada para permitir a atualização dos dados de um filme já cadastrado.

Foi implementada uma listagem numerada dos filmes, permitindo que o usuário escolha qual registro deseja modificar. Após a seleção, os valores do dicionário correspondente são atualizados diretamente.

### Motivo:

A estrutura anterior não permitia selecionar e modificar individualmente os filmes armazenados na lista.

### Resultado:

O sistema passou a permitir a atualização dos atributos de um filme específico, mantendo os demais registros da lista.

## REF04 - Implementação da exclusão de filmes

### Alteração:

A opção 4 do menu foi adaptada para permitir a exclusão de um filme selecionado pelo usuário.

Foi utilizada a listagem numerada para identificar o registro e o método `pop()` para removê-lo da lista por meio de seu índice.

### Motivo:

A estrutura anterior não possuía uma operação que permitisse excluir individualmente os filmes cadastrados.

### Resultado:

O sistema passou a permitir a exclusão de filmes específicos da lista, reorganizando automaticamente os índices dos elementos restantes.
