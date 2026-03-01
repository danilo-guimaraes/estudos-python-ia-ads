from random import randint  # Importa gerador de números aleatórios para simular notas
from time import sleep  # Importa função para criar pausas e melhorar a experiência do usuário

# Lista de dicionários representando o banco de dados de funcionários (Simulação de Database)
lista_estagiarios = [
    {"nome": "João", "salario": 1500, "Python": randint(0, 10)},
    {"nome": "Maria", "salario": 1500, "Python": randint(0, 10)},
    {"nome": "Pedro", "salario": 1500, "Python": randint(0, 10)},
    {"nome": "Ana", "salario": 1500, "Python": randint(0, 10)},
    {"nome": "Lucas", "salario": 1500, "Python": randint(0, 10)},
]

print("--- SISTEMA DE PROMOÇÃO SALARIAL ---")
sleep(0.5)

# O laço 'for' percorre cada estagiário individualmente (Iteração)
for estagiario in lista_estagiarios:
    print(f"\nAnalisando perfil de {estagiario['nome']}...")
    sleep(1.2)  # Pausa dramática para simular processamento do sistema

    # Lógica de ADS: Alta Performance (Nota acima de 8)
    if estagiario['Python'] > 8:
        estagiario['salario'] *= 1.20  # Atualiza o salário original com +20%
        print(f"✅ EXCELENTE! Nota {estagiario['Python']}. Aumento de 20% aplicado.")
        print(f"Novo salário: R${estagiario['salario']:.2f}")

    # Lógica de ADS: Bom Desempenho (Nota entre 5 e 8)
    elif estagiario['Python'] >= 5:
        estagiario['salario'] *= 1.10  # Atualiza o salário original com +10%
        print(f"🟡 BOM TRABALHO! Nota {estagiario['Python']}. Aumento de 10% aplicado.")
        print(f"Novo salário: R${estagiario['salario']:.2f}")

    # Caso a nota seja abaixo de 5 (Candidato em desenvolvimento)
    else:
        print(f"❌ NOTA {estagiario['Python']}. Sem aumento. Continue estudando Python!")
        print(f"Salário mantido: R${estagiario['salario']:.2f}")

print("\n--- Processamento de Folha Finalizado com Sucesso ---")

print("\n--- Processamento de Folha Finalizado ---")
