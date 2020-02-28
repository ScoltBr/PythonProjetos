"""
Dinionarios

OBS: Em algumas linguagens de programação, os dicionários Python são conhecidos
por mapas.

Dicionários são coleções de tipo chave/valor.

Dicionários são representados por chaves {}.

print(type({}))

OBS: Sobre dicionários
    - Chave e valor são separados por dois pontos 'chaves:valor';
    - Tanto chave quanto valor podem ser de qualquer tipo de dado;
    - Podemos misturar tipo de dados;

# Criação de dicionários

# Forma 1 (Mais comum)

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

print(paises)
print(type(paises))

# Forma 2 (Menos comum)
paises = dict(br= 'Brasil', eua='Estados Unidos', py='Paraguai')

print(paises)
print(type(paises))

# Acessando elementos

# Forma 1 - Acessando via chave, da mesmo forma que lista/tupla
print(paises['br'])
# print(paises['ru'])

# OBS: Vaso tentamos fazer um acesso utilizando uma chave que não existe, teremos o erro KeyError

# Forma 2 - Avessando via get - Recomendada

print(paises.get('eua'))
russia = paises.get('ru')

"""
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

pais = paises.get('py')

if pais:
    print(f'Encontrei o país {pais}')
else:
    print('Não encontrei o país')

# Podemos definir um valor padrão para caso não encontremos
pais = paises.get('py', 'Não encontramos')

print(f'Encontrei o pais {pais}')
