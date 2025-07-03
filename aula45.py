salas = [

    ['Maria', 'Helena', 'Sabrina', ],

    ['Elaine' ],

    ['Luiz', 'João', 'Eduarda', (10, 20, 30, 40, 50, 60, 70)],

]


# print(salas[2][3][1])


for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)