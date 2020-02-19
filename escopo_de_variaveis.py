"""
Escopo de variavel

Dois casos de escopo:

1 - Variáveis globais:
   - Variáveis globais são reconhecidas, ou seja, seu escopos compreendem, todo a o programa.

2 - Variáveis locais:
    - Variáveis locais ~soa reconhecidas apenas no bloco onde foram declarades, ou seja, seu escopo
    esta limitado ao seu bloco onde foi declarada

Para declarar variáveis em Python fazemos:

nome_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinâmica. Isso significada que
ao declararmos a variável, nos não colocamos o tipo de dado dela.
Este tipo é inferido ao atribuirmos o valor a mesma.

Exemplo em C:
int numero = 42;

Exemplo em Java:
int numero = 42;
"""
numero = 42
print(numero)
print(type(numero))

numero = 'Luiz'
print(numero)
print(type(numero))

nao_existo = 'Oi'
print(nao_existo)

numero =42

if numero > 10:
    novo = numero + 10 # A variavel 'novo' esta declarada localmente dentro do bloco do if. Portanto, é local
    print(novo)


print(novo)
