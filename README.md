## Calculadora de Reajuste Salarial e Bônus

Programa em Python desenvolvido para automatizar o cálculo de reajuste salarial e bonificação de funcionários.

## Regras de Negócio

Salário-mínimo de referência: R$ 1302,00.

Reajuste Salarial:

Até 2 salários-mínimos (até R$ 2604,00): Reajuste de 6,45%.

Mais de 2 até 5 salários-mínimos (R$ 2604,01 a R$ 6510,00): Reajuste de 4,55%.

Mais de 5 até 10 salários-mínimos (R$ 6510,01 a R$ 13020,00): Reajuste de 2,89%.

Acima de 10 salários-mínimos (acima de R$ 13020,00): Sem reajuste (0,00%).

## Bonificação por Assiduidade:

0 faltas: Bônus integral de 1 salário-mínimo (R$ 1302,00).

1 falta: Bônus fixed de R$ 500,00.

Mais de 1 falta: Sem bônus (R$ 0,00).

## Funcionalidades

Validação de Entrada:

Bloqueia salários negativos exibindo mensagem de erro e finalizando o programa sem solicitar dados adicionais.

Tratamento de Dados Inválidos:

Normaliza automaticamente valores negativos na quantidade de faltas para zero (0).

Geração de Relatório Executivo:

Exibe no terminal os dados organizados contendo: Salário Base, Salário Reajustado, Bônus e Ganho Total.

Formatação monetária padronizada com duas casas decimais.

## Tecnologias Utilizadas

Linguagem: Python 3

## Conceitos Aplicados:

Estruturas condicionais compostas e aninhadas (if, elif, else)

Operadores aritméticos e relacionais

Entrada e saída formatada de dados (f-strings)
