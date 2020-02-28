"""
Listas

Listas em Python funcional como vetores/matrizes (arrays) em outras linguagens, com a diferença
de serem DINÂMICO de podermos colocar QUALQUER tipo de dado.

Linguagens C#/Java: Arrays
    - Possuem tamanho e tipo de dado fixo:
    Ou seja, nestas linguagens se você criar um array do tipo int e com tamanho 5, este arry
    será SEMPRE do tipo inteiro e poderá ter no máximo 5 valores.

Já em Python:

- Dinâmico: Não possuem tamanho fixo; Ou seja, podemos criar a lista e simplesmente ir adicionando elementos;
- Qualquer tipo de dado: Não possuem tipo de dado fixo; Ou seja, podemos colocar qualquer tipo de dado;

As listas em Python são representadas por colchetes: []

# Podemos facilmente checar se determinado valor está contido na lista
num = 7
if 8 in lista4:
    print('Encontre o número 8')
else:
    print('Não encontrei o número 8')
# Podemos facilmente ordenar uma lista
lista1.sort()
print(lista1)

# Podemos facilmente contar o número de ocorrência de um valor em uma lista
print(lista1.count(1))
print(lista5.count('e'))

# Adicionar elementos em listas


#Para adicionar elementos em listas, utilizamos a função append


print(lista1)
lista1.append(42)
print(lista1)

# OBS: Com append, nós só conseguimos adicionar 1 elemento por vez
# lista1.append(12, 34, 56) # Erro

lista1.append([8, 3, 11])
print(lista1)

if [8, 3, 1] in lista1:
    print('Encontrei a lista')
else:
    print('Não encontrei a lista')

lista1.extend([123, 44, 67])
print(lista1)

# Podemos inserir um novo elemento na lista informando a posição do índice
# e podemos facilmente juntar duas listas

lista1 = lista1 + lista2
#   lista1.extend(lista2)
print(lista1)

lista1.reverse()
lista2.reverse()

print(lista1)
print(lista2)

# Forma 2
print(lista1[::-1])
print(lista2[::-1])

# Copiar uma lista
lista6 = lista2.copy()
print(lista6)

# Podemos contar quantos elementos existem dentro da lista
print(len(lista5))

# Podemos remover facilmente o último elemento de uma lista
# OBS: o pop não somente remove o último elemento mas também o retorna
print(lista5)
lista5.pop()
print(lista5)

# Podemos remover um elemento pelo indice
# OBS: Os elementos á direita deste serão deslocados para a esquerda.
# OBS: Se não houver elemento no indice informado teremos o erro IndexError.

lista5.pop(5)
print(lista5)

"""
type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['L', 'u','i', 'z', ' ', 'E','d', 'u','a','r','d','o']
lista3 = []
lista4 = list(range(11))
lista5 = list('Luiz Eduardo')
