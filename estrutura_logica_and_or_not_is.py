"""
Estrutura Lógicas: and (e), or(ou), not(não), is(é)

Operadores unários:
  - not;
Operadores binários:
  - and, or, is

Regras de funcionamento:

Para o 'and', ambos os valores precisam ser True
Para o 'or', um ou outro precisa ser True
Para o 'not', o valor do booleano é invertido, ou seja, se for True, vira False, se for False vira True
"""
ativo = True
logado = False

if not ativo:
    print('Você precisa ativar sua conta, por favor, cheque seu e-mail')
else:
    print('Bem-vindo usuário')

#print(not False)