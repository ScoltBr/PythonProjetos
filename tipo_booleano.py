"""
Tipo Booleano
Álgebra Booleana, criada por George Boole

2 constantes, Verdadeiro ou falso

True -> Verdadeiro
False -> Falso

OBS: Sempre com inicial maiuscula

Errado:

true, false

Certo:

True, False
"""
ativo = True;

print(ativo)

"""
Operações básicas: (Muito importante)
"""

# Negação (not):
"""
Fazendo a negação, se o valor boooleano for verdadeiro o resultado será falso,
se for falso o resultado será verdadeiro. ou sera sempre o contrário.
"""
# "not" é a mesma coisa do "!" no Java e C#

print(not ativo)
logado = False

# Ou (or):
"""
É uma operação binária ou seja depende de dois valores. um ou outro deve ser verdadeiro.

True or True -> True
True or False -> True
False or True -> True
False or False -> False

Igual o "||" do Java ou C#
"""
print(ativo or logado)

# E (and):

"""
Também é uma operação binária, ou seja, depende de dois valores.
Ambos os valores devem ser verdeiros.
 
True and True -> True
True and False -> False
False and True -> False
False and False -> False

Igual "&&" no Java ou C#
"""



