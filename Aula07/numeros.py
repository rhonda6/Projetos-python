"""
programa para mostrar números inteiros por extênso
somente números inteiros de 1 a 100
array = use o simbolo de [] para alterar valores
tuple = use o simbolo de () somente leitura, tem a performance mais rapida.
"""

from os import system
system("cls")
dezenas = ("", "dez", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "novaventa")
numeros = ("zero","um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", 
            "dez", "onze", "doze", "treze", "quatroze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove")

valor = input("Informe um número de 1 a 99: ")
numerico = int(valor)

#print(numeros[numerico])
extenso = ""
if(numerico < 20):
    #print(numeros[numerico])
    extenso = numeros[numerico]
elif(numerico < 100):
    #print(dezenas[int(valor[0:1])],"e", numeros[int(valor[1:2])])
    extenso = dezenas[int(valor[0:1])]
    if(valor[1:2] != "0"):
        extenso = f"{extenso} e {numeros[int(valor[1:2])]}"

print(extenso)


