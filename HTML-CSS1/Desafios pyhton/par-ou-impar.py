import time

print("Bem vindos ao aplicativo cuja única funcionalidade")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
print("é descobrir se o número é par ou ímpar! (digite 0 para acabar... acabar com o loop BRUTAL)")

time.sleep(2)

x = None

par = 0
impar = 0

while x != 0:
    try:
        x = int(input("Qual seu numero: "))

    except:
        print("Digite a porra de um numero!")
        continue #faz o programa rodar o loop denovo
            
    if x == 0:
        break

    time.sleep(1)

    if x % 2 == 0:
        par += 1
        print("Seu número é PAR")
    else:
        impar += 1
        print("Seu número é ÍMPAR")

print("Numeros pares:", par)
print("Numeros impares:", impar)
   

    



