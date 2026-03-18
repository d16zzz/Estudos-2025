cargo = input("Qual o seu cargo? ") #.strip().lower()
dia = input("Qual o dia da semana? ") #.strip().capitalize()

if (cargo == "supervisor" or cargo == "estagiario") and (dia == "Segunda" or dia == "Terça" or dia == "Quarta" or dia == "Quinta" or dia == "Sexta"):
    print("Acesso liberado")
elif cargo == "gerente" and (dia == "Sabado" or dia == "Domingo" or dia == "Segunda" or dia == "Terça" or dia == "Quarta" or dia == "Quinta" or dia == "Sexta"):
    print("Acesso liberado")
else:
    print("Acesso negado")
