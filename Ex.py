def parImpar(num):
    num = int(num)
    resto = num % 2
    if resto == 0:
        print("O número é par!")
    else:
        print("O número é ímpar!")

numero = input("Digite um número: ")
parImpar(numero)