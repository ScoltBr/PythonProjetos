"""
Funções com retorno

numeros = [1, 2, 3]

ret_pop = numeros.pop()

print(f'Retorno de pop: {ret_pop}')

ret_pr = print(numeros)

print(f'Retono de print: {ret_pr}')

OBS:  Em Python, quando uma função não retorna nenhum valor, o retorno é None

OBS: Funções em Python que retornam valores, devem retornar ester valores com a
palavra reservada return

OBS: Não precisamos necessariamente criar uma variavel para receber o retorno
de um função, Podemos passar a execução para outras funções
"""

#Exemplo função

def quadradp_de_7():
    #print(7 * 7) Sem retorno
    return 7 * 7 # Com retorno

# Criamos uma variavel para receber o retorno da função
ret = quadradp_de_7()
print(f'Retono {ret}') # Sem retorno resultado seria None