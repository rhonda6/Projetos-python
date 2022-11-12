from os import system
system("cls")

numero = input("Informe um número: ")
if(numero.isnumeric() == True):
    print("isto é um numero")
    numero = int(numero)
    #print(numero % 2) #mod resto da divisão

    if((numero % 2) == 1):
        print("Este número  é impar")
    else:
        print("Este número é par")

else:
    print('isto não é um numero')

print("Final do código")