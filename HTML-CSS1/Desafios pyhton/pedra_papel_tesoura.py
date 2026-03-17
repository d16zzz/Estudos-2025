print("--------------------------------------------------------------------------------")
print("Bem vindos ao jogo Pedra,Papel e tesoura, de um computador versus o humano!")
print("--------------------------------------------------------------------------------")

import random
import time
time.sleep(2)

opcoes = ["Pedra", "Papel", "Tesoura"]

escolha = input("QUAL A SUA ESCOLHA?")
escolha_maquina = random.choice(opcoes)
escolha_v = None ##VISUAL DELAS 🪨 Pedra, 📄 Papel, ✂️ Tesoura---
escolha_maquina_v = None ##VISUAL DELAS


escolha.lower()
escolha_maquina.lower()

time.sleep(2)
print("ESCOLHENDO O MEU...")
time.sleep(2)

if escolha == "pedra":
    escolha_v = "🪨"
elif escolha == "papel":
    escolha_v = "📄"
elif escolha == "tesoura":
    escolha_v = "✂️"


if escolha_maquina == "pedra":
    escolha_maquina_v = "🪨"
elif escolha_maquina == "papel":
    escolha_maquina_v = "📄"
elif escolha_maquina == "tesoura":
    escolha_maquina_v = "✂️"

print(f"Jogador: {escolha_v} | Máquina: {escolha_maquina_v}")

time.sleep(1)

vencedor = None

regras = {
    "pedra":"tesoura",
    "papel":"pedra",
    "tesoura":"papel"
}

if escolha == escolha_maquina:
    vencedor = "Empate"

elif regras[escolha] == escolha_maquina:
    vencedor = "Jogador"

else:
    vencedor = "Maquina"

print(f"O VENCEDOR DESSA RODADA FOI" {vencedor})






