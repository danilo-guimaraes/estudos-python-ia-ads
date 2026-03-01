from random import randint  # Importa gerador de números aleatórios
from time import sleep  # Importa função para pausas no terminal

# Lista original de funcionários com salários e notas geradas aleatoriamente
lista_funcionarios = [
    {"nome": "João", "salario": 1500, "Python": randint(0, 10)},
    {"nome": "Maria", "salario": 1500, "Python": randint(0, 10)},
    {"nome": "Pedro", "salario": 1500, "Python": randint(0, 10)},
    {"nome": "Ana", "salario": 1500, "Python": randint(0, 10)},
    {"nome": "Lucas", "salario": 1500, "Python": randint(0, 10)},
]

mantidos = []  # Lista para armazenar quem permanece na empresa

# Primeiro laço: Analisa cada funcionário individualmente
for funcionario in lista_funcionarios:
    sleep(1.2)  # Simulação de análise do sistema

    # Regra de ADS: Nota de Python maior ou igual a 4 para ser mantido
    if funcionario['Python'] >= 4:
        mantidos.append(funcionario)  # Adiciona à nova lista
        print(f"\nperfil de {funcionario['nome']} Mantido...")
    else:
        print(f"\nperfil de {funcionario['nome']} Cortado...")
        print('Motivo: Nota de Python abaixo de 4.')

    print('-----------------------------')

# --- Relatório Final Organizado ---
print('\n' + '=' * 30)
print('  RELATÓRIO FINAL DE EQUIPE  ')
print('=' * 30)

for funcionario in mantidos:
    print(f"-> Funcionário mantido: {funcionario['nome']}")

print('=' * 30)
print(f"Quantidade total de mantidos: {len(mantidos)}")

