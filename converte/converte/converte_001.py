"""
Programa converte_001
Descrição: Este programa converte uma medida inserida pelo usuário em metros para milímetros.
Autor: Pedro J. Tomazini
Data: 08/04/2026
Versão: 0.0.1
"""

# Alocação de memória

m = 0.0
i = 0

# Entrada e processamento de dados

while i==0:
    try:
        m = float(input("Insira uma medida em metros: "))
        if m>0:
            mv = m*1000 
            i = 1
        else:
            print("Insira um valor valido!")
    except:
        print("Insira um valor valido!")

# Saída de dados

print(f"O valor digitado em milimetros eh: {mv:.2f} mm")