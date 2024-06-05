import csv

alunos = [
    {"nome": "Alice", "idade": 14, "nota": 85},
    {"nome": "Bob", "idade": 15, "nota": 90},
    {"nome": "Charlie", "idade": 14, "nota": 78},
    {"nome": "David", "idade": 15, "nota": 88},
    {"nome": "Eve", "idade": 14, "nota": 92}
] # criando lista com os nomes

nome_arquivo = 'students.csv' # salva o nome para usar e criar arquivo

# Escrever os dados no arquivo CSV
with open(nome_arquivo, mode="w", newline="") as arquivo_csv:
    campos = ["nome", "idade", "nota"]
    escritor = csv.DictWriter(arquivo_csv, fieldnames=campos)
    escritor.writeheader()  # Escreve o cabeçalho

    for aluno in alunos:
        escritor.writerow(aluno)

print(f"Arquivo {nome_arquivo} criado com sucesso!")