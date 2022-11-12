"""
DocString
Aula 02 de python
Utilização de variáveis
28-10-2022
"""
import os
os.system("cls" if os.name == "nt" else "clear")

numero1 = input("Informe um número: ")
numero2 = input("Informe un segundo número: ")
numero3 = 55

print(type(numero1))
print(type(numero2))
print(type(numero3))

soma = int(numero1) + int(numero2)

print("A soma dos número é", soma)

print(type(numero1))

