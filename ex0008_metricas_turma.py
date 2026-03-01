from random import randint
from time import sleep

lista_funcionarios = [
    {"nome": "João", "salario": 1500, "Python": randint(0, 10)},
    {"nome": "Maria", "salario": 2200, "Python": randint(0, 10)},
    {"nome": "Pedro", "salario": 1800, "Python": randint(0, 10)},
    {"nome": "Ana", "salario": 2500, "Python": randint(0, 10)},
    {"nome": "Lucas", "salario": 1600, "Python": randint(0, 10)},
]
print("\nEquipe: ", end="")  # Começa a frase sem pular linha
for funcionario in lista_funcionarios:
    sleep(0.5)
    # Se for o último da lista, coloca um ponto final, senão coloca vírgula
    if funcionario == lista_funcionarios[-1]:
        print(f"{funcionario['nome']}.", end="")
    else:
        print(f"{funcionario['nome']}, ", end="")
print()  # Só para pular uma linha depois que terminar a lista toda

print("\n--- PROCESSANDO MÉTRICAS DA EQUIPE ---")
sleep(1)

# --- CÁLCULOS MATEMÁTICOS (Lógica de ADS) ---
total_salarios = sum(f['salario'] for f in lista_funcionarios)
total_python = sum(f['Python'] for f in lista_funcionarios)
media = total_python / len(lista_funcionarios)
maior_nota = max(f['Python'] for f in lista_funcionarios)
destaque = max(lista_funcionarios, key=lambda f: f["Python"])["nome"]

print("\n========== RELATÓRIO GERENCIAL ==========")
sleep(1)

print(f"💰 Total da Folha: R${total_salarios:.2f}")
sleep(1)

print(f"📊 Média Python da Equipe: {media:.1f}")
sleep(1)

print(f"🏆 Destaque do Mês: {destaque}")
print(f"⭐ Nota de Conhecimento: {maior_nota}")
sleep(1.2)

print("==========================================")
print("SISTEMA FINALIZADO COM SUCESSO.")
