from os import system
system("cls")

tabuada = 20
largura = tabuada * 6
print("[ Tabuada de Pitagoras ]".center(largura,"*"))

for i in range(1,tabuada,1):
    linha = f"|{i:>3} |"    
    for coluna in range(1,tabuada,1):
        linha += f" {i*coluna:>3} |"
    print(linha)

print("".center(largura,"*"))