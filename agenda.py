import sqlite3
import time
import os
import sys

if getattr(sys, 'frozen', False):
    diretorio_atual = os.path.dirname(sys.executable)
else:
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))

caminho_banco = os.path.join(diretorio_atual, 'database', 'agenda.db')

conectar = sqlite3.connect(caminho_banco)

cursor = conectar.cursor() 

def criar_tabela():
    cursor.execute("CREATE TABLE IF NOT EXISTS cadastro (Nome text, Telefone varchar(15), email text, data text)")
    
try: 
    criar_tabela()
except sqlite3.Error as erro:
    print("Erro ao criar a tabela: ", erro)
else:
    print("Tabela criada com sucesso!")

def inserir_dados(nome, telefone, email, data):
    cursor.execute("INSERT INTO cadastro VALUES (?, ?, ?, ?)", (nome, telefone, email, data))
    conectar.commit()
    print("Dados inseridos com sucesso!")

def menu():
    print(30 * '=')
    print('''
        Selecione uma opção:
        
        1 - Cadastrar
        2 - Pesquisar
        
        ''')
    print(30 * '=')

def operacao(op):
    if op == 1:
        while True:
            print("CADASTRO")
            time.sleep(3)
            data = time.strftime("%d/%m/%Y") 
            nome = input("Digite o nome:  (digite 'sair' para sair do cadastro) ")
            if nome.lower() == "sair":
                break
            telefone = input("Digite o telefone: ")
            email = input("Informe o email: ")
            inserir_dados(nome, telefone, email, data)
            print("Cadastro realizado com sucesso!")
        menu()
        opcao = int(input("Qual opção deseja: "))
        operacao(opcao)
    elif op == 2:
        print("Pesquisa por nome!")
        nome = input("Digite o nome: ")
        cursor.execute("SELECT * FROM cadastro WHERE Nome = ?", (nome,))
        resultados = cursor.fetchall()  # Retorna uma lista com todos os registros encontrados
        for linha in resultados:
            print(linha)
        menu()
        opcao = int(input("Qual opção deseja: "))
        operacao(opcao)
    else:
        print("Opção inválida!")
        menu()
        opcao = int(input("Qual opção deseja: "))
        operacao(opcao)


menu()
opcao = int(input("Qual opção deseja: "))
operacao(opcao)
