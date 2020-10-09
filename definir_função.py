"""
    Definindo Funções

- Funções são pequenas partes de código que realizam tarefas específicas;
- Pede ou não receber estradas de dados e retornar yna saída de dados;
- Muito uteis para executar procedimentos similares por repetidas vezes;

OBS: Se você escrever uma função que realiza várias tarefas dentro dela
é bom fazer uma verificação para que a função seja mais simplificada.


DICA: Fazer com que a função tenha um unico objetivo e não varios fazer uma organização do codigo
e facil leitura que é muito importante em empresas.

Já utilizamos várias funções desse github:
- print()
- len ()
- max ()
- min ()
- count ()
- e varias outras
"""

#Exemplo de utilização de funções:

cores = ['verde', 'amarelo', 'azul', 'branco']

# Utilizando a função integrada (Built-in) do python print()

print(cores)

curso = "Programação em Python é ESSENCIAL"

print(curso)

cores.append('roxo')

print(cores)

# curso.append('Mais dados...') #AttributeError
# print(curso)

cores.clear()
print(curso)

#print(help(print))
# DRY - Não repita você mesmo