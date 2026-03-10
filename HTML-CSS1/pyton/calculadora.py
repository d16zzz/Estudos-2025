print("Seja bem vindo a minha calculadora de numeros básicos")
a = float(input("Primeiro Numero:"))
b = float(input("Segundo Numero:"))
c = input("Escolha a operação desejada: (Divisao = :| Multiplicação = .| Subtração = -| Soma = +|")
resultado = int()

if c == ":":
    resultado = (a/b)

elif c == ".":
    resultado = (a*b)

elif c == "-":
    resultado = (a-b)

elif c == "+":
    resultado = (a+b)

print(f"O resultado é: {resultado : g}")
# print(f"O resultado da soma é: {(a+b):g}")