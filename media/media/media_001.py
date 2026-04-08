"""
Programa media_001
Descrição: Este programa faz a média de dois ou mais números reais.
Autor: Pedro J. Tomazini
Data: 07/04/2026
Versão: 0.0.1
"""

# Alocação de memória

v1 = 0.0
soma = 0.0
i = 0

# Entrada e processamento de dados
qtd = int(input("Qual sera a quantidade de numeros para media: "))

if qtd>=1:
    while i<qtd: 
        v1 = float(input("Digite o numero: "))
        soma = soma + v1
        i = i + 1
    med = soma/qtd
else:
    print("Erro! Digite uma quantidade valida.")

# Saída de dados
print(f'A media eh {med:5.2f}')