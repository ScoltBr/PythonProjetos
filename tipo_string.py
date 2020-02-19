"""
Tipos string

Em Python, um dado é considerado do tipo string sempre que:

- Estiver entre aspas simples -> 'uma string', '234', 'a', 'True', '42.3'
- Estiver entre aspas duplas ->  "uma string", "234", "a", "True", "42.3"
- Estiver entre aspas simples triplas -> '''uma string''', '''234''', '''a''', '''True''', '''42.3'''

nome = "Ginas's Bar"
print(nome)
print(type(nome))

nome = "Angelina \nJolie"            #\n server para pular de Linha
print(nome)
print(type(nome))

nome = 'Luiz Eduardo'
print(nome.upper()) # Para deixar todas as letras maiusculas

nome = 'Luiz Eduardo'
print(nome.lower()) # Para deixar todas as letras minusculas

nome = 'Luiz Eduardo'
print(nome.split()) # Transforma em uma lista de Strings

nome = 'Luiz Eduardo'
print(nome[0:4]) #Slice de string

"""
# Estiver entre aspas duplas triplas -> """uma string""", """234""", """a""", """True""", """42.3"""
nome = 'Luiz Eduardo'

"""
[::-1] -> Começa do primeiro elemento, vá até o último elemento e inverta
"""
print(nome[::-1])

print(nome.replace('L', 'F')) #Trocar um elemento por outro
