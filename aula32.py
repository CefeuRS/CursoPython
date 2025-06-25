""" Calculadora com while """
while True:#PARA QUE FUNCIONE O WHILE SEMPRE TEM QUE SER TRUE (FINALIZANDO COM BREAK)
    numero_1 = input('Digite um número: ')#PEÇA O PRIMEIRA NUMERO PARA O USUARIO
    numero_2 = input('Digite outro número: ')#PEÇA O SEGUNDIO NUMERO PARA O USUARIO
    operador = input('Digite o operador (+-/*): ')#PEÇA UM OPERADOR PARA QUE SEJA FEITA A CONTA

    numeros_validos = None#FLAG PARA VERIFICAR SE OS NUMEROS SÃO VALIDOS.

    num_1_float = 0#DEFININDO AS VARIAVEIS
    num_2_float = 0#DEFININDO AS VARIAVEIS

    try:
        num_1_float = float(numero_1)#AMBOS OS NUMEROS SÃO FLOAT, OU SEJA NÃO SÃO LIMITADOS A NUMEROS INTEIROS.
        num_2_float = float(numero_2)
        numeros_validos = True#AQUI A FLAG MARCARA QUE SÃO VERDADEIROS E PODERÁ PROSSEGUIR
    except:
        numeros_validos = None#SE CAIR AQUI É POR CONTA DOS NUMEROS SÃO INVALIDOS.

    if numeros_validos is None:#E CAIRÁ AQUI, DIZENDO QUE OS NUMEROS ESTÃO ERRADOS
        print('Um ou ambos os números digitados são inválidos.')
        continue#UTILIZADO PARA PARAR O LAÇO E COMEÇAR NOVAMENTE O CODIGO, E NÃO DAR CONTINUIDADE PRA BAIXO

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:#APOS A CHECAGEM DOS OPERADORES SE FOREM ERRADOS, CAIRÁ AQUI.
        print('Operador inválido.')
        continue#NOVAMENTE O CONTINUE PARA REINICIAR O CODIGO E NÃO IR AFRENTE.

    if len(operador) > 1:#PARA CASO A PESSOA DIGITE MAIS DE UM OPERADOR. LEN FAZ A VERIFICAÇÃO DO NUMERO DE ITENS DIGITADOS.
        print('Digite apenas um operador.')
        continue#NOVAMENTE O CONTINUE PARA REINICIAR O CODIGO E NÃO IR AFRENTE.

    print('Realizando sua conta, confira os resultados abaixo: ')

    if operador == '+':
        print(f'{num_1_float}+{num_2_float}=', num_1_float + num_2_float) #f-string para mostrar a informação dos numeros
    elif operador == '-':
        print(f'{num_1_float}-{num_2_float}=', num_1_float - num_2_float)
    elif operador == '*':
        print(f'{num_1_float}*{num_2_float}=', num_1_float * num_2_float)
    elif operador == '/':
        print(f'{num_1_float}/{num_2_float}=', num_1_float / num_2_float)
    else:
        print('Nunca deveria chegar aqui')

    sair = input('Quer sair? [s]im: ').lower().startswith('s')#LOWER TEM A FUNÇÃO DE RETORNAR TUDO EM MINUSCULO
#STARTSWITH(.) VERIFICA SE UMA RESPOSTA COMEÇA COM A LETRA SELECIONADA NOS PARENTESES
#ENDSWITH(.) VERIFICA SE UMA RESPOSTA DO USUARIO TERMINA COM A SEGUINTE LETRA.
#SE A RESPOSTA DO USUARIO FOR CORRETA COM A LETRA, DARÁ TRUE, SE NÃO DARÁ FALSE.
    if sair is True:
        break#NESSE CASO SE ELE DIGITAR A LETRA CORRETA. O IF SERA ACIONADO E ACIONARA O BREAK.FINALIZANDO A OPERAÇÃO.