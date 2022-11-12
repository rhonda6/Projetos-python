"""
Calculo area do retangulo

"""
import os
os.system("cls")

print(f"{'*'*10} Calculo da area do retangulo {'*'*10}\n")
print("Informe o primeiro lado: ")
lado1 = input()

print("Informe o segundo lado: ")
lado2 = input()

# variável.isnumeric = verifica se a variável pode ser um numero inteiro
# variável.isdecimal = verifica se a variável pode ser um numero com casas decimais

print("O primeiro valor é número inteiro ? ", lado1.isnumeric())
print("O segundo valor é número inteiro ? ", lado2.isnumeric())
print("Será que vai dar certo ou vai dar erro ?")

#int = converte o valor do variavel em inteiro
#float = converte o valor da variável em float (decimal)

area = int(lado1) * int(lado2)

print("Area do triangulo é {} m² sendo os dados {} x {} ".format(area, lado1, lado2))
print("Area do triangulo é",area, "m² sendo os dados", lado1, "x", lado2) 