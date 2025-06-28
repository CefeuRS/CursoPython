for i in range(11): #O RANGE VAI DE 0 A 10 (O ULTIMO NÃO APAREÇE)
    if i == 2: #O I MOSTRARÁ NA LINHA CORRESPONDENTE
        print('i é 2, pulando...')
        continue#APÓS MOSTRAR, CONTINUARÁ

    # if i == 8:
    #     print('i é 8, seu else não executará')#POR CONTA DO BREAK QUANDO CHEGAR NO 8, A FUNÇÃO IRÁ PARAR
    #     break

    for j in range(1, 3):#A FUNÇÃO J DEFINE QUE A COLUNA IRA REPITIR 2 VEZES
        print(i, j)#LEMBRANDO QUE SE É 1, 3 A ULTIMA NÃO APAREÇE
else:
    print('For completo com sucesso!')