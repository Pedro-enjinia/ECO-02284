"""
Programa soma_estruturada001
Descrição: Executa a soma de dois números inteiros inseridos pelo usuário, utilizando o controle de fluxo de execução 'while'.
Autor: Pedro J. Tomazini
Data: 07/04/2026
Versão: 0.0.1
"""

# Alocação na memória

s1 = 0
soma = 0

# Entrada de dados

while s1<2:
    i = int(input(f"Insira um valor: "))
    soma = soma + i
    s1 = s1+1

# Processamento de dados

# Saída de dados

print(f"O resultado da soma entre os dois numeros eh: {soma}")