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

"""
Em Python, a forma geral de definir uma função é:

def nome_da_função(parametros_de_entrada)
    bloco_da_função

Onde:

nome_da_função -> SEMPRE, com letra minúscula, e se for nome composto, separare por underline (Snake case);
parametros_de_entrada -> Opcional, onde tede mais de um, cada um separado por virgula (','), podendo ser opcionais ou não;
bloco_da_função -> Também chamado de corpo da função ou implementação, é onde o processamento da função acontece;
Nesse bloco, pode ter ou não retorno da função

OBS: Veja que para definir uma função, utilizamos a palavra reservada 'def' informando ao Python que estamos
definindo uma função. Também abrimos o bloco de código com o já conhecido dois pontos (':') que é utilizado
em Python para definir blocos. 
"""

#Definindo a primeira função

# Definição

def diz_oi():
    print('Oi!')

"""
OBS:

1 - Veja que, dentro das nossas funções podemos utilizar outras funçoes;
2 - Veja que nossa função só executa 1 tarefa, ou seja, a única coisa que ela fez é dizer oi;
3 - Veja que esta função não recebe nenhum parâmetro de entrada;
4 - Veja que esta função não retorna nada;
"""

# Utilizado funções

# Chamada de execução
# diz_oi()

"""
Atenção:

Nunca esqueça de utilizar os parènteses ao executar uma função.

Exemplo:
# Errado!
diz_oi

# Certo
diz_oi()

# Errado
diz_oi ()
"""

# Exemplo 2

def cantar_parabens():
    printf('Parabéns para você')
    printf('Nesta data querida')
    printf('Muitas felicidades')
    printf('Muitos anos de vida')

#for n in range(4):
#    cantar_parabens()

# Em python, podemos inclusive criar variáveis do tipo de uma função e executar esta função através da varável

cantar = cantar_parabens()

cantar()
