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
   conexao, cursor = conectar_banco()
   
   id_contato = input("Digite o ID do contato a ser atualizado: ")

   sql = "SELECT * FROM contatos WHERE id = ?"

   cursor.execute(sql, (id_contato,))
   
   contato = cursor.fetchone()

   if contato == None:
       print("Contato não encontrado.")
       conexao.close()
       return

   print("Contato encontrado:")
   print(f"Nome: {contato[1]}")
   print(f"Telefone: {contato[2]}")
   print(f"Email: {contato[3]}")     

   novo_nome = input("Digite o novo nome: ")
   novo_telefone = input("Digite o novo telefone: ")
   novo_email = input("Digite o novo email: ")

   sql = "UPDATE contatos SET nome = ?, telefone = ?, email = ? WHERE id = ?"

   cursor.execute(sql, (novo_nome, novo_telefone, novo_email, id_contato))

   conexao.commit()

   conexao.close()

   print("Contato atualizado com sucesso!")


def excluir_contato():
    conexao, cursor = conectar_banco()

    id_contato = input("Digite o ID do contato a ser excluído: ")

    sql = "SELECT * FROM contatos WHERE id = ?"

    cursor.execute(sql, (id_contato,))

    contato = cursor.fetchone()

    if contato == None:
        print("Contato não encontrado.")
        conexao.close()
        return

    print("Contato encontrado:")
    print(f"Nome: {contato[1]}")
    print(f"Telefone: {contato[2]}")
    print(f"Email: {contato[3]}")

    confirmacao = input("Tem certeza que deseja excluir este contato? (s/n): ")

    if confirmacao.lower() == "s":
        sql = "DELETE FROM contatos WHERE id = ?"
        cursor.execute(sql, (id_contato,))
        conexao.commit()
        print("Contato excluído com sucesso!")
    else:
        print("Exclusão cancelada.")

    conexao.close()


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