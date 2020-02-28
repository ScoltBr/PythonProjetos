"""
Loop for

Loop -> Estrutura de repetição
For -> Uma dessas estruturas

C# ou Java

 for(int i = 0; i < 10; i++){
    //execução do loop
 }

 Python
 for item in interavel:
  //execução do loop


Utilizamos loop para iterar sobre sequências ou sobre valores iteráveis

 Exemplos de iteráveis:
 - String
   nome = 'Luiz Eduardo'
 - Lista
    lista = [1, 3, 5, 7, 9]
 - Range
   numeros = range(1, 10)

   # Exemplo de for l (Iterator em uma string)
for letras in nome:
    print(letras)

# Exemplo de for 2 (Iterando sobre uma lista)
for numero in lista:
    print(numero)

# Exemplo de for 3 (Iterando sobre um range)
for numero in range(1, 100):
    print(numero)


range(valor_inicial, valor_final)

OBS: O valor final não é inclusive.
1
2
3
4
5
6
7
8
9
10 - Não

for numero in range(1, 10):
    print(numero)


((0, 'L'), (1, 'u'), (2, 'i') (3, 'z') ....)

 for indice, letras in enumerate(nome):
   print(nome[indice])

 for valor in enumerate(nome):
   print(valor)

   qnt = int(input('Quantas vezes esse loop deve rodar? '))
soma = 0

for n in range(1 , qnt+1):
    num = int(input(f'Informe o {n}/{qnt} valor: '))
    soma = soma + num
print(f'A soma é {soma}')

nome = 'Luiz Eduardo'
for letra in nome:
    print(letra, end='')

Tabela de Emojis Unicode: https://apps.timwhitlock.info/emoji/tables/unicode
"""
# Original: U+1F60D
# Modificado: U0001F60D

#emoji = 'U0001F60D'

for x in range(3):
    for num in range(1, 11):
     print('\U0001F60D' * num)