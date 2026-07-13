import sqlite3
import time

conectar = sqlite3.connect('database/agenda.db') # Cria o banco de dados ou importa caso já exista

cursor = conectar.cursor() # Cria o cursor para manipular o banco de dados, é uma ferramenta que permite executar comandos SQL

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
            data = time.strftime("%d/%m/%Y") # 
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
    else:
        print("Opção inválida!")


menu()
opcao = int(input("Qual opção deseja: "))
operacao(opcao)


 
