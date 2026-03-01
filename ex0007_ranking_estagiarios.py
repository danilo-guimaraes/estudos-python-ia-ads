from random import randint

candidatos = [
    {"nome": "Bruno", "nota": randint(0, 10)},
    {"nome": "Carla", "nota": randint(0, 10)},
    {"nome": "Diego", "nota": randint(0, 10)},
    {"nome": "Fernanda", "nota": randint(0, 10)},
    {"nome": "Gabriel", "nota": randint(0, 10)},
]

# Ordena do maior para o menor
candidatos.sort(key=lambda x: x['nota'], reverse=True)

print("🏆 OS 3 MELHORES (APROVADOS) 🏆")
for selecionado in candidatos[:3]:
    print(f"Parabéns {selecionado['nome']}! Você está no Top 3 com nota {selecionado['nota']}.")

print("\n📩 MENSAGEM PARA OS DEMAIS 📩")
# O [3:] começa a ler a lista a partir da 4ª posição em diante
for nao_selecionado in candidatos[3:]:
    print(f"Olá {nao_selecionado['nome']}, infelizmente você não entrou no Top 3 desta vez. Sua nota foi {nao_selecionado['nota']}.")