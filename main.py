import csv

alunos = [] # criando lista vazia para os nomes 
somaNotas = 0
mediaNotas = 0

nome_arquivo = 'students.csv' # salva o nome para usar e criar arquivo

# 2. Ler Dados do Arquivo CSV:
# Escreva um programa Python que lê os dados do arquivo students.csv e armazena-os em uma lista de dicionários. Use o comando "with open()".
with open(nome_arquivo, mode="r") as arquivo_csv:
    leitor = csv.DictReader(arquivo_csv)
    for linha in leitor:
        alunos.append(linha)

for aluno in alunos:
    print(f"Nome: {aluno['nome']}, Idade: {aluno['idade']}, Nota: {aluno['nota']}")
    # 3. Calcular Média das Notas
# Processar os dados lidos e calcular a média.

    somaNotas += int( aluno['nota'])




mediaNotas = somaNotas/len(alunos)

print(f"\nSomatorio das Notas: {somaNotas}")
print(f"Media das notas: {mediaNotas}")


# 4. Escrever Dados Processados em um Novo Arquivo CSV:
# Escreva um programa que grava os dados dos alunos, incluindo a média das notas, em um novo arquivo CSV chamado students_with_average.csv.

nome_arquivo_salvamento = 'students_with_average.csv'

for aluno in alunos:
    aluno["media_notas"] = mediaNotas

# Escrever os dados no arquivo CSV
with open(nome_arquivo_salvamento, mode="w", newline="") as arquivo_csv:
    campos = ["nome", "idade", "nota", "media_notas"]
    escritor = csv.DictWriter(arquivo_csv, fieldnames=campos)
    escritor.writeheader()  # Escreve o cabeçalho

    for aluno in alunos:
        escritor.writerow(aluno)

print(f"Arquivo {nome_arquivo} criado com sucesso!")


# 5. Verificar o Arquivo de Saída:
# Verifique o arquivo students_with_average.csv para garantir que os dados foram gravados corretamente.



# def velidar(alunosOriginal):    
#     nome_arquivo_salvamento = 'students_with_average.csv'
#     alunos_verificar = []

#     with open(nome_arquivo_salvamento, mode="r") as arquivo_csv:
#       leitor = csv.DictReader(arquivo_csv)
#       for linha in leitor:
#           alunos_verificar.append(linha)

#   if alunosOriginal == alunos:
#     print("Salva")


# velidar(alunos)