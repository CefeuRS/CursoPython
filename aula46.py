"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""


def soma(x, y, z):#PARAMETRO É A DEFINIÇÃO DA FUNÇÃO, OU SEJA DA VARIAVEL
    # Definição
    print(f'{x=} y={y} {z=}', '|', 'x + y + z = ', x + y + z)

#ARGUMENTO É O VALOR QUE EU PASSO PARA A VIRIAVEL
soma(1, 2, 3)#ARGUMENTO NÃO NOMEADO (ARGUMENTO POSICIONAL)DEVEM SER PASSADOS NA MESMA ORDEM DOS PARAMETROS
soma(1, y=2, z=5)#ARGUMENTO NOMEADO (PODEM SER PASSADOS FORA DE ORDEM DA VARIAVEL)

print(1, 2, 3, sep='-')