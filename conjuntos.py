"""
Conjuntos

- Conjuntos em qualquer linguagem de programção, estamos fazendo referencia à Teoria dos Conjuntos
da Matemática

- Aqui no Python, os conjuntos são chamados de Sets.

Dito isso, da mesma forma que na matemática:

- Sets (conjuntos) não possuem valores duplicados;
- Sets (conjuntos) não possuem valores ordenados;
- Elementos não são acessados via índice, ou seja, conjuntos não são indexados;

Conjuntos são bons para se utilizar quando precisamos armazenar elementos
mas não nos importamos com a ordenação deles. Quando não precisamos se preocupar
com chaves, valores e itens duplicados

Os conjuntos (sets) são referenciados em Python com {}

Diferença entre Conjuntos (Set) e Mapas (Dicionários) em Python:
        - Um dicionário tem chave/valor;
        - Um conjunto tem apenas valor;

# Definindo um conjunto?

# Forma 1

s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3})

print(s)
print(type(s))

# OBS: Ao criar um conjunto, caso seja adicionado um valor já existente o mesmo
# será ignorado sem gerar error e não fará parte do conjunto.

# Forma 2

s = {1, 2, 3, 4, 5, 5}
print(s)
print(type(s))

if 3 in s:
    print('Tem o 3')
else:
    print('Não tem o 3')
"""
# Importante lembrar que, além de não termo valores duplicados, não temos ordem

s = {99, 2, 34, 23, 12, 1, 44, 5}