# Agenda de Contatos em Terminal (SQLite3 & Python)

Este é um projeto prático desenvolvido durante o aprendizado de Python (Seção 8 do Curso de Python). Trata-se de uma aplicação de linha de comando (CLI) que simula uma agenda de contatos, utilizando o banco de dados **SQLite3** para persistência dos dados de forma local.

O projeto também conta com suporte a empacotamento, tendo sido gerado um executável de terminal através da biblioteca `auto-py-to-exe`.

## 🚀 Funcionalidades

- **Criação Automática de Banco de Dados:** O sistema verifica e cria a tabela `cadastro` automaticamente no primeiro início.
- **Cadastro de Contatos:** Permite salvar Nome, Telefone, E-mail e armazena automaticamente a Data do cadastro.
- **Busca Avançada:** Permite pesquisar contatos salvos no banco de dados filtrando pelo Nome.
- **Fluxo Contínuo:** Menu interativo baseado em terminal que permite realizar múltiplas operações sem fechar o programa.

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **SQLite3** (Módulo nativo do Python para banco de dados relacional)
- **Time** (Módulo nativo para manipulação de datas e temporizadores)
- **Auto PY to EXE** (Utilizado para converter o script `.py` em um executável `.exe`/binário)

## 📂 Estrutura do Banco de Dados

A tabela `cadastro` possui a seguinte estrutura:

| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| **Nome** | TEXT | Nome do contato |
| **Telefone** | VARCHAR(15) | Número de telefone formatado |
| **email** | TEXT | Endereço de e-mail |
| **data** | TEXT | Data de inclusão (DD/MM/AAAA) |
