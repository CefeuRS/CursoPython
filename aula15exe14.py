entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')
senha_permitida = '123456'

print(entrada)

#TUDO QUE ESTIVER DENTRO DE PARENTESES É LIDO PRIMEIRO
# OR VERIFICA OUTRAS CONDIÇÕES PARA CONFIRMAÇÃO
#AND ADICIONA OUTRAS VERIFICAÇÕES
if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar com sucesso')
else:
    print('Incorreto, Você saiu.')

print(True and False)
print(False or 0 or 0.0 or 'abc')






