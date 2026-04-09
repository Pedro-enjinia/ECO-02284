"""
Programa termometro_001
Descrição: Este programa avalia se a temperatura do ambiente está agradável.
Autor: Pedro J. Tomazini
Data: 08/04/2026
Versão: 0.0.1
"""

# Alocação de memória

temp: int = 0

# Entrada de dados

temp = int(input("Digite a temperatura ambiente: "))

# Saída de dados

if temp>0 and temp<=18:     # Temperaturas negativas não foram classificadas
    print("Clima frio.")

elif temp>18 and temp<=28:
    print("Clima agradavel.")

elif temp>28:
    print("Clima quente.")

else:
    print("Digite um valor valido!")