import os

lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('cls')#LIMPA O PAINEL, MOSTRANDO APENAS O VALOR A SER INSERIDO
        valor = input('Valor: ')#PEDE O VALOR A SER INSERIDO
        lista.append(valor)#ADICIONA MAIS UM VALOR AO FINAL DA LISTA
    elif opcao == 'a':#CASO SELECIONADO, IRA PEDIR O INDICE PARA SE APAGAR
        indice_str = input(
            'Escolha o índice para apagar: '
        )

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:#TRATA UM ERRO, MOSTRANDO AO USUARIO QUE ALGO DEU ERRADO
            print('Por favor digite número int.')
        except IndexError:#TRATA UM ERRO, MOSTRANDO AO USUARIO QUE ALGO DEU ERRADO
            print('Índice não existe na lista')
        except Exception:#TRATA UM ERRO, MOSTRANDO AO USUARIO QUE ALGO DEU ERRADO
            print('Erro desconhecido')

    elif opcao == 'l':
        os.system('cls')#LIMPA O PAINEL, MOSTRANDO APENAS O VALOR A SER INSERIDO

        if len(lista) == 0:#CASO A VERIFICAÇÃO DA LISTA RETORNE 0, O CODIGO RETORNARÁ ESSA MENSAGEM
            print('Nada para listar')

        for i, valor in enumerate(lista):#SE SELECIONADO, COM O LEN, IRA MOSTRAR A LISTAGEM DOS ITENS INSERIDOS
            print(i, valor)
    else:
        print('Por favor, escolha i, a ou l.')