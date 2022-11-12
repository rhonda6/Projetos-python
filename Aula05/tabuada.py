from os import system, name
from pydoc import doc
system("cls")


#print("Digite o número para calcular a tabuada: ")

#numero = input("->")
#while not numero.isnumeric():
#    print("Digite o número para calcular a tabuada: ")
#    numero = input("->")
tabuada = 10

for i in range(11):
   
   #antigamente era a melhor pratica
   #print("{}*x{}={}".format(tabuada, i, (tabuada * i))) 

   #melhor pratica
   print(f"{tabuada: >2} x {i: >2} = {(tabuada * i): >3}") 

   #nao fazer isso
   #print(tabuada,"x",i,"=",tabuada*i)