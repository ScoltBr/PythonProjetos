""""
Tipo float

Tipo real, dicimal

Casas decimais

OBS: o separados de casas de cimais na programação é o ponto e não a virgula. [1.5F,0.9F,1.123F]
"""

# Errado do ponto de vista do Float, mas gera uma tupla
from builtins import int

valor = 1, 44                                                                      #Tuple
print(valor)
print(type(valor))

# Certo

valor = 1.44
print(valor)
print(type(valor))

# É possivel
valor1, valor2 = 1,44
print(type(valor1))
print(type(valor2))

# Podemos converter um float para um int
"""
OBS: Ao converter valores float para inteiros, nos perdemos precisão.
"""
res = int(valor)
print(res)
print(type(res))

# Podemos trabalhar com numeros complexos

varialvel = 5j






