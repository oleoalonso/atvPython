# Leonardo L. Alonso Carriço
# leonardo@carrico.com.br

# Exercício Prático Python 03

###################################################################
# 3) 3.	Faça um programa que leia um nome de usuário e a sua senha 
# e não aceite a senha igual ao nome do usuário, 
# mostrando uma mensagem de erro e voltando a pedir as informações.

nome = input("\nEntre com o seu nome : ")
senha = input("Entre com a sua senha : ")

if nome == senha :
    print("\nErro! A senha informada é igual ao nome\n")
else:
    print("\nUsuário / Senha salvo com sucesso!\n") 