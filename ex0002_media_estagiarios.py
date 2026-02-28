from random import randint  # Importa função para gerar números inteiros aleatórios

lista = [
    {'nome': 'Danilo', 'idade': 18, 'python': True, 'nota': randint(5, 10)},  # Lista de dicionários com notas aleatórias
    {'nome': 'Gael', 'idade': 20, 'python': False, 'nota': randint(1, 10)},
    {'nome': 'Maria', 'idade': 17, 'python': True, 'nota': randint(3, 8)}
]

soma_notas = 0  # Inicializa acumulador de notas
for i in lista:  # Percorre cada estagiário na lista
    soma_notas += i['nota']  # Soma a nota do estagiário atual ao total
    status = "Apto" if i['python'] and i['idade'] >= 18 else "Inapto"  # Lógica simplificada de status
    print(f"Nome: {i['nome']} | Nota: {i['nota']} | Status: {status}") # Exibe os dados formatados

media = soma_notas / len(lista)  # Calcula a média dividindo o total pelo número de itens na lista
print(f"\nA média geral da turma ficou em: {media:.2f}") # Exibe a média com 2 casas decimais