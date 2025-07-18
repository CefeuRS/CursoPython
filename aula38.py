# Listas em Python
# Tipo list - Mutável
# Suporta vários valores de qualquer tipo
# Conhecimentos reutilizáveis - índices e fatiamento
# Métodos úteis:
#     append - Adiciona um item ao final
#     insert - Adiciona um item no índice escolhido
#     pop - Remove do final ou do índice escolhido
#     del - apaga um índice
#     clear - limpa a lista
#     extend - estende a lista
#     + - concatena listas
# Create Read Update   Delete
# Criar, ler, alterar, apagar = lista[i] (CRUD)
#        0   1   2   3
lista = [10, 20, 30, 40, 50, 60]
lista.append('Luiz')
nome = lista.pop()
lista.append(1233)
del lista[6]
# lista.clear()
lista.insert(3, 'Ola')
print(lista[3])