# Requisitos

## Requisitos funcionais 

- RF01 - O sistema deve permitir cadastrar filmes e suas informações.
- RF02 - O sistema deve permitir listar filmes e suas informações.
- RF03 - O sistema deve permitir atualizar informações.
- RF04 - O sistema deve permitir excluir filmes da lista.

## Regras de Negocio

- RN01 - A nota do filme deve estar entre 0 e 10. Caso contrario, o sistema deve informar que o valor deve estar entre 0 e 10.
- RN02 - O nome do filme nao pode ficar vazio. Caso fique vazio, o sistema deve informar que nao e possível cadastrar um filme sem colocar o nome.
- RN03 - A duração do filme deve ser maior que 0. Caso seja 0 ou um valor negativo, o sistema deve informar que o valor deve ser maior que 0.
- RN04 - O sistema deve classificar o filme de acordo com seu ano de lancamento. Caso o ano seja menor ou igual ao ano atual, o filme deve ser classificado como "Já lançado". Caso o ano seja maior que o ano atual, deve ser classificado como "Vai ser lançado".

## Requisitos Nao Funcionais

- RNF01 - O sistema deve ser executado por meio do terminal.
- RNF02 - O sistema deve possuir uma interface simples e fácil de utilizar.
- RNF03 - O sistema deve funcionar sem a necessidade de conexão com a internet.
- RNF04 - O sistema deve ser desenvolvido utilizando a linguagem Python.
