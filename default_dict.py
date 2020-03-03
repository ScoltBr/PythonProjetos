"""
Módulo Collections - Default Dict

# Recap Dicionários

dicionario =  {'Curso': 'Luiz Eduardo'}

print(dicionario)

print(dicionario['Curso'])

print(dicionario['outro']) # ??? KeyError

Default Dict ->  Ao criar um dicionário utilizando-o, nós informamos um valor dafult,
podemos utilizar um lambda para isso. Este valor será utilizado sempre que não houver
um valor definido. Caso tentemos acessar uma chava que não existe, essa chave será
criada e o valor default será atribuido

OBS: Lambdas são funções sem nome, podem ou não receber parâmetros de entrada
e retornar valores
"""

# Fazendo import

from collections import defaultdict

dicionario = defaultdict(lambda : 0)

dicionario['curso'] = 'Luiz Eduardo'

print(dicionario['outro']) # ??? KeyError
print(dicionario)