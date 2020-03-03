"""
Módulo Collections - Counter

Collections -> High-performance Container Datetypes

Counter -> Recebe um interável com parâmetro e cria um objeto do tipo Collections Counter que é parecido
com um dicionário, contendo como chave o elemento da lista passada com parâmetro e com valor e quantidade
de ocorrência desse elemento.


# Utilizando o Counter

from collections import Counter

# Exemplo 1

lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 5, 5, 5, 3, 45, 45, 66, 66, 43, 34]

# Utilizando o Counter
res = Counter(lista)

print(res)
print(type(res))

# Counter({1: 5, 3: 5, 2: 4, 4: 3, 5: 3, 45: 2, 66: 2, 43: 1, 34: 1})

# Veja que, para cada elemento da lista, o Counter criou uma chave e colocou com o valor a quantidade de ocorrências.

# Exemplo 2

print(Counter('Luiz Eduardo'))
# Counter({'u': 2, 'd': 2, 'L': 1, 'i': 1, 'z': 1, ' ': 1, 'E': 1, 'a': 1, 'r': 1, 'o': 1})
"""

from collections import Counter

# Exemplo 3

texto = """Mussum Ipsum, cacilds vidis litro abertis. Mé faiz elementum girarzis, nisi eros vermeio.
 Delegadis gente finis, bibendum egestas augue arcu ut est. Paisis, filhis, espiritis santis.
  Interessantiss quisso pudia ce receita de bolis, mais bolis eu num gostis.
"""
palavras = texto.split()

# print(palavras)

res = Counter(palavras)
print(res)

# Econtra as 5 palavras com mais ocorrências no texto
print(res.most_common(5))