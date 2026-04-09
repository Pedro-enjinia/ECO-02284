"""
Programa bhaskara_001
Descrição: Este programa retorna as raízes do polinômio de segundo grau, cujo usuário informou os coeficientes.
Autor: Pedro J. Tomazini
Data: 08/04/2026
Versão: 0.0.1
"""

# Alocação de memória

i: int = 0
a: float = 0
b: float = 0
c: float = 0

# Entrada de dados

print("Este programa retorna as raizes de polinomio do tipo:\n\n{:^54}\n".format("a*x^2 + b*x + c = 0"))

while i==0:
    try:
        a = float(input("Insira o valor do coeficiente 'a': "))
        b = float(input("Insira o valor do coeficiente 'b': "))
        c = float(input("Insira o valor do coeficiente 'c': "))
        i = 1
    
    except:
        print("Algum valor inserido está incorreto, tente novamente.")

# Processamento de dados

delta = b**2-4*a*c

if delta==0:
    r1 = r2 = -b/(2*a)

elif delta>0:
    r1 = (-b+delta**0.5)/(2*a)
    r2 = (-b-delta**0.5)/(2*a)

elif delta<0:
    r1 = (-b+((-delta)**0.5)*1j)/(2*a)
    r2 = (-b-((-delta)**0.5)*1j)/(2*a)

else: # Caso consiga passar de alguma forma da primeira verificação
    print("Erro! Reinicie o programa.")

# Saída de dados

print(f"As raizes são:\n{r1}\n{r2}")