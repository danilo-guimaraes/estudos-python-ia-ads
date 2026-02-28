from random import randint  # Importa gerador de números aleatórios
from time import sleep  # Importa função para pausar a execução

lista_estagiarios = [  # Banco de dados inicial
    {'nome': 'Danilo', 'idade': 18, 'python': True, 'nota': randint(5, 10)},
    {'nome': 'Gael', 'idade': 20, 'python': False, 'nota': randint(1, 10)},
    {'nome': 'Maria', 'idade': 17, 'python': True, 'nota': randint(3, 8)}
]

while True:  # Loop de validação de entrada de nome
    busca = input('Digite o nome: ').capitalize()  # Recebe o nome e coloca a primeira letra em maiúscula
    if busca.replace(' ', '').isalpha():  # Verifica se contém apenas letras
        break  # Sai do loop se estiver correto
    print("❌ Erro: Use apenas letras para o nome.")

achou = False  # Variável de controle (flag) para busca
for etg in lista_estagiarios:  # Varre a lista procurando o nome
    if busca == etg['nome']:  # Se encontrar o nome digitado
        print(f"\n✅ Estagiário encontrado! \nIdade: {etg['idade']} | Nota: {etg['nota']}")
        achou = True  # Marca que o candidato foi encontrado
        break  # Interrompe o loop

if not achou:  # Se a flag continuar False após o loop
    print(f'\n⚠️ Estagiário {busca} não encontrado.')
    add = (input(f'Deseja adicionar {busca}? (s/n): ')).lower()

    if add in ['s', 'sim']:  # Verifica se a resposta foi positiva
        while True:  # Loop para validar idade numérica
            idade_in = input('Digite a idade: ')
            if idade_in.isdigit():  # Verifica se são apenas números
                idade = int(idade_in)  # Converte o texto para inteiro
                break
            print("❌ Erro: Digite apenas números.")

        python_in = input('Sabe Python? (s/n): ').lower()
        python = True if python_in in ['s', 'sim'] else False  # Converte resposta para Booleano

        nota = randint(4, 10)  # Gera uma nota aleatória para o novo cadastro
        lista_estagiarios.append({'nome': busca, 'idade': idade, 'python': python, 'nota': nota})  # Adiciona à lista
        print(f'\n✅ {busca} cadastrado com sucesso com nota {nota}!')