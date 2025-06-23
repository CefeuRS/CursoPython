usuario = input('[Nilton] Digite seu nome de usuário para entrar: ')

# Aceita apenas 'Nilton' ou 'nilton', ignorando maiúsculas e minúsculas
if usuario.lower() == 'nilton':
    print('Carregando...') 
else:
    print('Usuário inválido. Reinicie o programa.')  # Encerra para nomes inválidos.

# Define a senha correta que será usada para comparação 
senha_permitida = '13245768'

# O usuário terá 5 tentativas para acertar a senha 
for tentativa in range(5):  # Loop que será executado no máximo 5 vezes
    senha = input("Digite a senha: ")  # Solicita ao usuário que digite a senha
    
    # Verifica se a senha digitada está correta
    if senha == senha_permitida:  
        print("Senha correta! Acesso liberado.")  # Mensagem de sucesso
        break  # Encerra o loop porque a senha está correta
    else:
        # Mensagem informando que a senha está incorreta e exibindo a tentativa atual
        print(f"Senha incorreta. Tentativa {tentativa + 1} de 5.")  
else:
    # Este bloco será executado se o loop for finalizado sem que a senha correta seja digitada
    print("Todas as tentativas foram usadas. Acesso bloqueado.")
