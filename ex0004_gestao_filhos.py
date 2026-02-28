# Criando uma lista que contém dicionários para organizar os dados dos filhos
children = [
    {"name": "Gael", "age": 4, "lives_with_me": True},  # Armazena nome, idade e se mora junto (Gael)
    {"name": "Maria", "age": 6, "lives_with_me": True},  # Armazena nome, idade e se mora junto (Maria)
    {"name": "Alice", "age": 8, "lives_with_me": False}  # Armazena dados da Alice (mora com a mãe)
]

# Iniciando um laço 'for' para percorrer cada 'filho' (dicionário) dentro da lista 'children'
for child in children:

    # Verificando se o valor da chave 'lives_with_me' é Verdadeiro (True)
    if child["lives_with_me"]:
        # Se for True, imprime que mora com você usando uma f-string para formatar o texto
        print(f"{child['name']} is {child['age']} years old and lives with me.")

    # Caso a condição acima seja Falsa (False), o código executa este bloco
    else:
        # Imprime que a criança vem passar as férias (lógica aplicada para a Alice)
        print(f"{child['name']} is {child['age']} years old and comes for the holidays.")