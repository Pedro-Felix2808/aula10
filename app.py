import sqlite3


def conectar_banco():
    conexao = sqlite3.connect("contatos.db")
    cursor = conexao.cursor()

    sql = '''
    CREATE TABLE IF NOT EXISTS contatos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        telefone TEXT NOT NULL,
        email TEXT NOT NULL
    )
    '''

    cursor.execute(sql)
    conexao.commit()

    return conexao, cursor


def cadastrar_contato(nome, telefone, email):
    conexao, cursor = conectar_banco()

    sql = '''
    INSERT INTO contatos (nome, telefone, email)
    VALUES (?, ?, ?)
    '''

    cursor.execute(sql, (nome, telefone, email))

    conexao.commit()
    conexao.close()


def listar_contatos():
    conexao, cursor = conectar_banco()

    sql = "SELECT * FROM contatos"

    cursor.execute(sql)

    contatos = cursor.fetchall()

    conexao.close()

    if len(contatos) == 0:
        print("Nenhum contato encontrado.")

    else:
        print("### LISTA DE CONTATOS ###")

        print(
            f"{'ID':<5} | {'Nome':<20} | {'Telefone':<15} | {'Email':<30}"
        )

        print("-" * 80)

        for contato in contatos:
            print(
                f"{contato[0]:<5} | "
                f"{contato[1]:<20} | "
                f"{contato[2]:<15} | "
                f"{contato[3]:<30}"
            )


def buscar_contato(nome):
    conexao, cursor = conectar_banco()

    sql = "SELECT * FROM contatos WHERE nome LIKE ?"
    cursor.execute(sql, (f"%{nome}%",))

    contatos = cursor.fetchall()

    conexao.close()

    if len(contatos) == 0:
        print("Nenhum contato encontrado.")

    else:
        print("### RESULTADO DA BUSCA ###")

        print(
            f"{'ID':<5} | {'Nome':<20} | {'Telefone':<15} | {'Email':<30}"
        )

        print("-" * 80)

        for contato in contatos:
            print(
                f"{contato[0]:<5} | "
                f"{contato[1]:<20} | "
                f"{contato[2]:<15} | "
                f"{contato[3]:<30}"
            )

def atualizar_contato():
    print("funcao para atualizar contato")


def excluir_contato():
    print("funcao para excluir contato")


def menu():

    while True:

        print()
        print("### CONTATOS ###")
        print("1 - Cadastrar contato")
        print("2 - Listar contatos")
        print("3 - Buscar contato pelo nome")
        print("4 - Atualizar contato")
        print("5 - Excluir contato")
        print("6 - Sair")

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":

            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o telefone do contato: ")
            email = input("Digite o email do contato: ")

            cadastrar_contato(nome, telefone, email)

            print("Contato cadastrado com sucesso!")

        elif opcao == "2":

            listar_contatos()

        elif opcao == "3":

            nome = input("Digite o nome do contato a ser buscado: ")
            buscar_contato(nome)

        elif opcao == "4":

            atualizar_contato()

        elif opcao == "5":

            excluir_contato()

        elif opcao == "6":

            print("Saindo do programa...")
            break

        else:

            print("Opção inválida. Tente novamente.")


menu()