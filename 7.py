print("Seja bem-vindo")
nome = print(input ("informe seu nome: "))
print("Ola")
a = float(input("Informe a primeira nota: "))
b = float(input("Informe a segunda nota: "))

d = (a+b)/2

if(d>= 7):
    print("você passou, média:",d)

if(d < 7):
    print("Sua média está baixa, média:",d)

if(d > 10):
    print("Você digitou algum número errado, média:",d)