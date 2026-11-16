# 📓 LOGBOOK AFP — Algoritmos e Programação (2026.2)

# 1. CAMPO 01 — INSTRUMENTO DE ENTRADA

### 1a. Objetos de conhecimento

- Lógica de programação;
- Variáveis;
- Funções;
- Estruturas condicionais;
- Operadores lógicos.

### 1b. Lacunas de conhecimento

Como eu estava começando a programar, conhecia alguns conceitos, mas ainda tinha dificuldade para aplicá-los na prática. Minhas principais lacunas eram:

- Compreender e aplicar laços de repetição, principalmente `while` e `for`;
- Entender como funcionam listas e dicionários;
- Compreender como utilizar o método `append()` para adicionar elementos a uma lista.

### 1c. Hipótese inicial

O principal problema do sistema era a limitação no armazenamento dos dados.  
O programa conseguia guardar apenas um filme por vez.  
Isso acontecia porque os dados eram armazenados em variáveis individuais.  
Eu acreditava que o sistema precisava utilizar estruturas capazes de armazenar vários registros.  
Por isso, considerei que listas e dicionários poderiam solucionar essa limitação.

---

# 2. CICLO 01 — PREPARAÇÃO DO LABORATÓRIO E ESCOLHA DO PROJETO

### 1. Desafio do ciclo

Configurar o ambiente de desenvolvimento, familiarizar-me com as ferramentas necessárias para programar e definir um projeto que permitisse aplicar, de forma prática, os fundamentos de algoritmos e programação.

### 2. O que implementei

Escolhi desenvolver um catálogo de filmes inspirado na Netflix, por ser a primeira ideia que surgiu. Inicialmente, organizei os requisitos do projeto e, em seguida, comecei a desenvolver o código.

Não tenho, neste momento, os nomes dos arquivos e os commits específicos dessa etapa para registrar como evidência.

### 3. Objetos de conhecimento mobilizados

- Python;
- Ambiente de desenvolvimento;
- Visual Studio Code (VS Code);
- Git;
- GitHub;
- Versionamento de código;
- Levantamento de requisitos.

Eu ainda não tinha experiência prática com programação, pois nunca havia escrito uma linha de código. Também estava começando a aprender a utilizar as ferramentas de desenvolvimento e versionamento.

### 4. Desvio ou erro encontrado + causa técnica

Não tive dificuldades na instalação do ambiente. Entretanto, encontrei dificuldades na utilização do GitHub, principalmente para organizar o repositório. Acabei realizando muitos commits, pois ainda não tinha familiaridade com o processo de versionamento e organização das alterações.

### 5. Decisão de ajuste + fonte

Comecei organizando os requisitos antes de escrever o código, para ter uma ideia do que o sistema deveria realizar. Como referência para o aprendizado de Python, utilizei o livro *Pense em Python*.

### 6. Feedback recebido

Não recebi feedback ou orientação específica do professor ou de colegas nessa etapa.

### 7. Próximo passo

Começar a desenvolver as funcionalidades do catálogo, aplicando os conceitos iniciais de variáveis, tipos de dados e entrada e saída de informações.

---

# 3. CICLO 02 — VARIÁVEIS, TIPOS DE DADOS E ENTRADA/SAÍDA

### 1. Desafio do ciclo

Compreender como receber, armazenar e manipular os dados dos filmes por meio de variáveis e tipos de dados, desenvolvendo as primeiras funcionalidades do CRUD e identificando uma forma adequada de organizar os registros.

### 2. O que implementei

Desenvolvi as operações iniciais do CRUD, trabalhando com as informações necessárias para cadastrar e manipular os filmes. Cada filme possuía os seguintes campos:

- `nome`;
- `duracao`;
- `genero`;
- `sinopse`;
- `ano`;
- `nota`.

Inicialmente, utilizei variáveis individuais para armazenar os dados. O usuário digitava as informações solicitadas e as variáveis recebiam os valores.

### 3. Objetos de conhecimento mobilizados

- Variáveis;
- Tipos de dados;
- Entrada de dados com `input()`;
- Saída de dados com `print()`;
- Conversão de tipos com `int()` e `float()`;
- Atribuição de valores;
- Strings, inteiros e números decimais.

### 4. Desvio ou erro encontrado + causa técnica

Uma das dificuldades foi lembrar de converter os valores recebidos pelo `input()` para os tipos adequados. A duração e o ano precisavam ser convertidos para `int`, enquanto a nota precisava ser convertida para `float`.

Outra dificuldade importante foi perceber que a estrutura inicial permitia armazenar apenas um filme por vez. O uso de variáveis individuais não era suficiente para representar uma coleção de vários filmes.

### 5. Decisão de ajuste + fonte

Com o auxílio da inteligência artificial, consegui compreender como utilizar uma lista de dicionários para armazenar vários filmes. A lista passou a reunir os registros, enquanto cada dicionário representava um filme com seus respectivos campos.

Utilizei principalmente a IA para esclarecer dúvidas e compreender como aplicar esses conceitos, além do livro *Pense em Python* como material de estudo.

### 6. Feedback recebido

Não houve feedback específico do professor ou de colegas registrado nessa etapa. As dificuldades foram trabalhadas principalmente por meio de estudo e auxílio da IA.

### 7. Próximo passo

Aprofundar o entendimento sobre operadores, organização lógica do programa e programação procedural, buscando compreender melhor como as instruções são executadas.

---

# 4. CICLO 03 — OPERADORES, FLUXOGRAMAS E PARADIGMAS

### 1. Desafio do ciclo

Aplicar operadores de atribuição e comparação na construção da lógica do sistema, compreendendo como as expressões influenciam a execução das instruções e como organizar o programa seguindo o paradigma procedural.

### 2. O que implementei

Utilizei operadores de atribuição e comparação na construção da lógica do sistema. Também trabalhei com a organização das instruções para que o programa executasse as ações de acordo com as escolhas do usuário.

Não foram desenvolvidos fluxogramas nessa etapa.

### 3. Objetos de conhecimento mobilizados

- Operador de atribuição (`=`);
- Operador de igualdade (`==`);
- Operador de diferença (`!=`);
- Expressões relacionais;
- Programação procedural;
- Organização sequencial de instruções;
- Estruturas de controle.

Uma das distinções importantes foi compreender que `=` atribui um valor a uma variável, enquanto `==` compara dois valores.

### 4. Desvio ou erro encontrado + causa técnica

Em alguns momentos, tive confusão entre os operadores `=` e `==`, principalmente por serem visualmente semelhantes. Entretanto, já conhecia a diferença conceitual entre atribuição e comparação.

Não tive problemas relacionados à precedência de operadores ou divisão por zero.

### 5. Decisão de ajuste + fonte

Busquei compreender melhor a função de cada operador e sua aplicação na lógica do programa. A organização procedural foi trabalhada por meio da sequência de instruções e da execução das ações conforme as condições estabelecidas.

Como referência de estudo, utilizei o conteúdo da disciplina e o livro *Pense em Python*.

### 6. Feedback recebido

Não recebi feedback específico do professor ou de colegas nessa etapa.

### 7. Próximo passo

Aplicar estruturas condicionais para controlar as escolhas do usuário e direcionar a execução do programa conforme cada opção selecionada.

---

# 5. CICLO 04 — ESTRUTURAS CONDICIONAIS

### 1. Desafio do ciclo

Implementar estruturas condicionais para controlar o fluxo de execução do CRUD, permitindo interpretar as escolhas do usuário, validar as opções do menu e direcionar corretamente cada operação do sistema.

### 2. O que implementei

Utilizei estruturas condicionais principalmente no menu do sistema. O usuário selecionava uma opção e o programa verificava essa escolha para executar a ação correspondente.

As condições permitiam direcionar a execução para diferentes funcionalidades do CRUD, como cadastro, listagem, atualização e exclusão de filmes.

### 3. Objetos de conhecimento mobilizados

- Estrutura condicional `if`;
- Estrutura condicional `elif`;
- Estrutura condicional `else`;
- Operadores relacionais;
- Expressões condicionais;
- Validação de entradas;
- Fluxo de execução;
- Indentação em Python.

### 4. Desvio ou erro encontrado + causa técnica

Durante o desenvolvimento, identifiquei algumas dificuldades na construção das estruturas condicionais.

- **Validação do menu:** o programa aceitava opções inválidas, pois as entradas do usuário não estavam sendo verificadas adequadamente.
- **Construção das condicionais:** algumas condições de `if` e `elif` estavam incorretas, prejudicando o direcionamento da execução.
- **Funcionamento das operações:** determinadas operações do CRUD não funcionavam como esperado devido à lógica condicional utilizada.

Esses problemas estavam relacionados à dificuldade de estruturar corretamente as condições e prever os diferentes caminhos que o programa poderia seguir.

### 5. Decisão de ajuste + fonte

Revisei a lógica das estruturas condicionais com auxílio da inteligência artificial. Durante esse processo, analisei as condições utilizadas, identifiquei os problemas e ajustei a lógica para que cada opção do menu direcionasse corretamente a execução.

Também utilizei o livro *Pense em Python* como material de apoio para estudar as estruturas condicionais e compreender melhor sua aplicação.

### 6. Feedback recebido

Não recebi feedback específico do professor ou de colegas nessa etapa.

### 7. Próximo passo

Continuar desenvolvendo e testando as funcionalidades do CRUD, buscando aprimorar a lógica de execução, a validação das entradas e o tratamento das diferentes situações que podem ocorrer durante a utilização do sistema.

---

# 6. CAMPO 02 — APROFUNDAMENTO

### 2a. Referências e contribuições para a solução

**1. Livro: Pense em Python**

Utilizei o livro como material de apoio para estudar os fundamentos da linguagem Python. Ele serviu como referência para compreender conceitos de programação e a utilização de estruturas da linguagem, complementando o conteúdo trabalhado em aula.

**2. Inteligência artificial**

Utilizei a IA principalmente como apoio para compreender conceitos e resolver dificuldades durante o desenvolvimento. Quando encontrava erros ou não conseguia aplicar determinado conteúdo, apresentava minhas dúvidas e buscava explicações que me ajudassem a entender como prosseguir.

A IA teve uma participação importante especialmente no entendimento de variáveis, listas e dicionários, pois eu ainda estava começando a programar e tinha dificuldade para transformar os conceitos em código.

### 2b. Revisão da hipótese inicial

Minha hipótese inicial era que o principal problema do CRUD estava relacionado à limitação do armazenamento, pois o sistema conseguia guardar apenas um filme por vez.

Após estudar e desenvolver a solução, compreendi melhor a causa técnica dessa limitação. O problema estava relacionado à forma como os dados eram organizados e armazenados. O uso de variáveis individuais não permitia administrar adequadamente vários registros.

A utilização de listas e dicionários mostrou-se mais adequada para resolver essa dificuldade.

A lista permite armazenar vários elementos em uma única estrutura, possibilitando reunir diversos filmes. Já o dicionário permite organizar as informações de cada filme por meio de pares de chave e valor, como `nome`, `duracao`, `genero`, `sinopse`, `ano` e `nota`.

Assim, minha hipótese inicial foi confirmada e aprofundada: não bastava armazenar os dados em variáveis, era necessário utilizar estruturas de dados capazes de representar uma coleção de registros.

### 2c. Dimensionamento inicial dos recursos

| Recurso | Quantidade estimada | Justificativa técnica |
|---|---|---|
| Tempo de estudo e desenvolvimento | Aproximadamente 8 horas inicialmente, embora tenham sido necessárias mais de 20 horas para compreender melhor os conteúdos | O desenvolvimento exigia estudar os fundamentos de Python e aplicar os conceitos no CRUD. |
| Execuções de teste | Inicialmente cerca de 15, mas foram realizadas 50 ou mais | Cada funcionalidade desenvolvida precisava ser executada para verificar se estava funcionando corretamente. |
| Operações do CRUD | 4 operações | Era necessário implementar cadastro, listagem, atualização e exclusão de filmes. |
| Campos por registro | 6 campos | Cada filme precisava armazenar nome, duração, gênero, sinopse, ano e nota. |
| Estruturas de dados principais | 2 estruturas | Uma lista para reunir os registros e um dicionário para organizar os dados de cada filme. |

**Observação sobre os testes:** não organizei formalmente os casos de teste em uma documentação. As verificações eram realizadas diretamente no sistema, utilizando as funcionalidades para observar se o comportamento estava correto. Por isso, a quantidade informada representa uma estimativa baseada na frequência com que executei o programa, e não um registro formal de testes individuais.
