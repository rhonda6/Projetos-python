from os import system
system("cls")

print("[ Calculadora IMC ]".center(50,"*"))
print("\n")

print("Informe o seu peso (em kg): ")
peso = input("-> ")

if(not peso.isdecimal()):
   print("O peso foi informado errado.")
   exit() # finaliza o código em python

print("Informe a sua altura (em centimetros): ")
altura = input("-> ")

if(not altura.isdecimal()):
   print("A altura está incorreta.")
   exit() # finaliza o código em python

#round  - arredondamento, no final colocar quantas casas decimais
imc = round(float(peso) / ((float(altura) / 100) ** 2), 2)
#imc = round(imc, 2)
print("\nINC: ",imc)

if(imc < 18.5):
    classificacao = "Baixo Peso"
elif(imc < 25):
    classificacao = "Euztrófico"
elif(imc < 30):
    classificacao = "Sobrepeso"
else :
    classificacao = "Obesidade"

print(classificacao.center(50,"#"))
