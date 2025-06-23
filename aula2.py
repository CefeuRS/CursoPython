print(12, 34, sep='-', end="\n") #Sep é o separador. end é o fim da linha
print(48, 10, sep='', end="\n") #\n é a quebra de linha
print(32, 12, 5, sep= "-")
print(2, 7665, sep= "-") #Se não tiver nada no separador, os objetos se juntam
print(2, 7665, sep= "-", end='\n') #Se não tiver nada no separador, os objetos se juntam
print(1, "Ola \"Roberto\"") #Escape, usado para por as "aspas" numa string
print("Ola 'Roberto'")

print ('Explicito','é','melhor-que-explicito.', sep='-')
print ('explicito','é','melhor " do que explicito' )
print (type(1))
print (type(1.5), type(6.7), type(7))
print (10 == 15)
print (type (10 == 15))
print (int('1'), type(int('1')))  #TYPE MOSTRA O TIPO QUE A FERAMENTA É (INT,BOOL,STR)

print (int('1') + 1) #INT NUMEROS INTEIROS (NESSE CASO AQUI O INT TRANSFORMOU O STR EM INT)
print (float('1') + 1) #FLOAT NUMEROS FLUTUANTES
#PODEM SER COLOCADOS NA FRENTE PARA SE MUDAR A FUNÇÃO