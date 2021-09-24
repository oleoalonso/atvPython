# Leonardo L. Alonso Carriço
# leonardo@carrico.com.br

# Exercício Prático Python 02

###################################################################
# 2) Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

letraDigitada = input("\nEntre com uma letra (M ou F) : ")

if letraDigitada == "M" or letraDigitada == "m" :
    print("\nM - Masculino\n")

elif letraDigitada == "F" or letraDigitada == "f" :
    print("\nF - Feminino\n")

else:
    print("\nLetra inválida\n")  