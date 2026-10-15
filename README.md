# Controle de Níveis de Água

## 1. Apresentação

Este projeto foi desenvolvido como atividade da **Agenda 11 da disciplina Desenvolvimento de Sistemas I**, do curso Técnico em Desenvolvimento de Sistemas da **ETEC EaD**.

O programa simula o monitoramento do nível de água de um reservatório, classificando sua situação em cinco níveis e exibindo mensagens coloridas no terminal.

## 2. Objetivo

Desenvolver um algoritmo em Python que permita identificar a situação de um reservatório de acordo com o nível de água informado pelo usuário.

O programa utiliza listas, funções, estruturas condicionais e a biblioteca `colorama` para apresentar as informações de maneira organizada e visual.

## 3. Tecnologias utilizadas

- **Python:** linguagem de programação utilizada no desenvolvimento do algoritmo.
- **Colorama:** biblioteca responsável por aplicar cores às mensagens exibidas no terminal.
- **Visual Studio Code:** editor utilizado para escrever e executar o programa.
- **GitHub:** plataforma utilizada para armazenar e compartilhar o projeto.

## 4. Classificação dos níveis de água

O programa trabalha com cinco níveis:

| Nível | Situação do reservatório | Cor |
|---|---|---|
| 1 | Muito baixo (crítico) | Vermelho |
| 2 | Baixo | Amarelo |
| 3 | Médio | Verde |
| 4 | Alto | Ciano |
| 5 | Muito alto (alerta) | Azul |

## 5. Funcionamento do algoritmo

O funcionamento do programa ocorre nas seguintes etapas:

1. Importa os recursos `Fore` e `Style` da biblioteca `colorama`.
2. Cria uma lista contendo as cinco situações possíveis do reservatório.
3. Define uma função responsável por identificar a cor correspondente a cada nível.
4. Solicita ao usuário que informe um número de 1 a 5.
5. Verifica se o número informado está dentro do intervalo permitido.
6. Calcula a posição da situação correspondente na lista.
7. Chama a função que determina a cor do nível informado.
8. Exibe a situação do reservatório na cor correspondente.
9. Restaura a formatação original do terminal.
10. Caso o número informado esteja fora do intervalo de 1 a 5, apresenta uma mensagem de nível inválido.

## 6. Conceitos de programação utilizados

**Variáveis:** armazenam os valores utilizados durante a execução do programa.

**Entrada de dados (`input`):** permite receber o nível de água informado pelo usuário.

**Listas:** armazenam as cinco situações possíveis do reservatório.

**Estruturas condicionais (`if`, `elif` e `else`):** permitem verificar condições e determinar quais instruções serão executadas.

**Operadores de comparação e lógicos:** são utilizados para verificar se o nível informado está dentro do intervalo permitido.

**Funções (`def` e `return`):** organizam a lógica responsável por determinar a cor correspondente ao nível de água.

**Bibliotecas:** permitem utilizar funcionalidades externas, como as cores disponibilizadas pela biblioteca `colorama`.

## 7. Como executar o programa

### Requisitos

- Python instalado no computador.
- Biblioteca `colorama` instalada.

### Instalação da biblioteca

Abra o terminal e execute:

```bash
python -m pip install colorama
```

### Execução

1. Abra a pasta do projeto no Visual Studio Code.
2. Abra o arquivo Python do algoritmo.
3. Execute o programa.
4. Digite um número de 1 a 5 quando solicitado.
5. Observe a situação do reservatório exibida na cor correspondente.

## 8. Exemplo de execução

**Entrada:**

```text
Informe o nível de água atual: 3
```

**Saída:**

```text
O valor digitado é: 3
Médio
```

A mensagem `Médio` será apresentada em verde no terminal.

### Exemplo de nível inválido

**Entrada:**

```text
Informe o nível de água atual: 6
```

**Saída:**

```text
O valor digitado é: 6
Nível inválido! Digite um número entre 1 e 5.
```

## 9. Testes realizados

O programa foi testado com os níveis de 1 a 5, apresentando corretamente as situações e cores correspondentes.

Também foi realizado um teste com o número 6, confirmando o funcionamento da validação de valores fora do intervalo permitido.

## 10. Considerações finais

O desenvolvimento deste projeto permitiu aplicar conhecimentos adquiridos ao longo da disciplina Desenvolvimento de Sistemas I, especialmente sobre variáveis, listas, funções, estruturas condicionais e utilização de bibliotecas em Python.

A atividade também contribuiu para compreender como diferentes recursos da linguagem podem ser combinados na construção de um programa funcional.