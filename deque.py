"""
Módulo Collections - Deque

Podemos dizer que o deque é uma lista de alta performace.
"""

# Importa
from collections import deque

# Criando deque

deq= deque('Luiz')
print(deq)

# Adicionando elementos no deque

deq.append('z') # Adiciona no final

print(deq)

deq.appendleft('K')

print(deq)

# Remover elementos

print(deq.pop()) # Remove e retorna o ultimo elemento
print(deq)

print(deq.popleft()) # Remove e retorna o primeiro elemento

print(deq)