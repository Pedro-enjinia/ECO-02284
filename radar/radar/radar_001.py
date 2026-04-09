"""
Programa radar_001
Descrição: Este programa pergunta ao usuário a velocidade do carro, caso ultrapasse 80 km/h, este será multado. Nesse caso, exibe o valor
da multa, cobrando R$ 5,00 por km acima de 80 km/h.
Autor: Pedro J. Tomazini
Data: 08/04/2026
Versão: 0.0.1
"""

# Alocação de memória

vel = 0.0

# Entrada de dados
try:
    vel = float(input("Insira sua velocidade atual: "))
    
except:
    print("Insira um valor valido!")

# Processamento e saída de dados

if vel>80:
    multa = (int(vel)-80)*5
    print(f"Voce esta multado!\nValor: R${multa:.2f}")

elif vel>0 and vel<=80:
    print("Muito bem, siga respeitando o limite de velocidade")

else:
    print("Insira um valor valido!")