from os import system
system("cls")
# criação de variável texto
# As variáveis devem seguir um padrão
# snake_case, PascalCase, camelCase
nome_completo = "Laercio Azevedo de Sá"
print(len(nome_completo)) #conta a quantidade de caracteres

print(nome_completo.count('e')) #encontra a repetição de um caracter
print(nome_completo.upper()) # todas as letras maiusculas
print(nome_completo.lower()) # todas as letras minusculas
print(nome_completo.capitalize()) #somente a primeira letra maiuscula
print(nome_completo.find(' ')) # procura o primeiro ocorrencia de espaço em branco

espaco = nome_completo.find(' ')
nome = nome_completo[0: espaco]
print(nome)

print(nome_completo.replace(' ','#')) # subistitui espaço em branco por #
print(nome_completo.center(80, "*"))
print(nome_completo.split(' '))

