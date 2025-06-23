#informe se este número é par ou ímpar. Caso o usuário não digite um númeroAdd commentMore actions
#inteiro, informe que não é um número inteiro.

entrada = input('Digite um número: ')

if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0 #COM INT SÓ ACEITA NUMEROS INTEIROS
    par_impar_texto = 'ímpar'

    if par_impar:
        par_impar_texto = 'par'

    print(f'O número {entrada_int} é {par_impar_texto}')
else:
    print('Você não digitou um número inteiro')

try:
    entrada_int = float(entrada)
    par_impar = entrada_int % 2 == 0 #COM FLOAT ACEITA NUMERO FLUTUANTE
    par_impar_texto = 'ímpar'

    if par_impar:
        par_impar_texto = 'par'

    print(f'O número {entrada_int} é {par_impar_texto}')
except:
    print('Você não digitou um número inteiro')

    #AMBAS AS FORMAS SÃO FORMULAS DO MESMO PROBLEMA
