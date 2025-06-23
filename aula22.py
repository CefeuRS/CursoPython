seu_nome = input('Digite o seu Nome: ')
sua_idade = input('Digite a sua idade: ')

if seu_nome and sua_idade:#PARA O IF ANALISAR TANTO UMA CONDIÇÃO QUANTO A OUTRA
    print(f'Seu Nome é: {seu_nome} ')#MOSTRANDO O NOME
    print(f'O seu nome invertido é: {seu_nome[::-1]} ') #FATIAMENTO


    if ' ' in seu_nome:#VERIFICA SE CONTEM ESPAÇOS NO NOME, IN MOSTRA LOCAL
        print('Seu nome contem espaços')
    else:
        print('Seu nome não contem espaços')

    print(f'O seu nome tem {len(seu_nome)} letras')#MOSTRA AS LETRAS DE UMA PALAVRA, SEJA STR OU VARIAVEL
    print(f'A primeira letra do seu nome é: {seu_nome[0]}')#INDICES MOSTRAM A LETRA CONFORME A ONDEM QUE ESTÃO
    print(f'A última letra do seu nome é: {seu_nome[-1]}')#NO CASO [-1] SENDO A ULTIMA E [0] SENDO A PRIMEIRA
else:
    print('Desculpe, voce deixou campos vazios')


#LEMBRANDO SEMPRE DE RESPEITAR A ORDEM DO PRIMEIRO IF E FECHAR COM O ELSE ABAIXO DE TUDO
#DENTRO DO BLOCO PODEM TER MAIS IF, ELIF E ELSE, POREM NAO PODEM PASSAR NA MESMA LINHA DOS PRIMEIROS.
