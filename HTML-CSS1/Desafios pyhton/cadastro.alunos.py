nome = []
notas = {}

# Entrada no sistema
while True:
    s = input("Quer entrar no sistema? (sim/nao): ").strip().lower()

    if s == "sim":
        sistema = True
        break
    elif s == "nao":
        sistema = False
        break
    else:
        print("Resposta inválida. Digite apenas 'sim' ou 'nao'.")

# Cadastro de alunos
while sistema == True:
    r = input("Voce quer adicionar um novo aluno? (sim/nao): ").strip().lower()

    if r == "nao":
        break
    elif r == "sim":
        nomes = input("Qual o nome desse aluno: ").strip()
        nome.append(nomes)
        print(f"A lista atual de alunos: {nome}")
    else:
        print("Digite apenas sim ou nao.")

# Verificação se tem aluno
if len(nome) == 0:
    print("Nenhum aluno cadastrado")
else:
    print("\nAlunos cadastrados:")
    for aluno in nome:
        print(aluno)

    # Atribuir notas
    index = 0
    while index < len(nome):
        nota = float(input(f"Qual a nota desse aluno ({nome[index]})? "))
        notas[nome[index]] = nota
        index += 1

    # Mostrar sistema atualizado
    print("\nSistema atualizado")
    print("ALUNO | NOTA")

    for aluno, nota in notas.items():
        print(f"{aluno} | {nota}")