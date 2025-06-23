nome = input('Digite o seu nome: ')
sobrenome = input('Digite o seu sobrenome: ')
tamanho_nome = len(nome)
tamanho_sobrenome = len(sobrenome)

if tamanho_nome > 1:
        print('Seu nome é muito curto')
elif tamanho_nome <=3:
        print('Seu nome é normal')
elif tamanho_nome >=5:
        print('Seu nome é muito grande')

if nome and sobrenome:
    print(f'Seu nome completo é: {nome} {sobrenome} ')
elif nome and not sobrenome:#AND NOT É SE A PESSOA NAO DIGITAR A OUTRA PARTE
    print('voce não digitou seu sobrenome')
elif sobrenome and not nome:
    print('voce não digitou seu nome')
    
else:
    print('Seu nome esta irregular')

