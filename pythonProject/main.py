ids = [1, 2]
nome = ['admim', 'usuario']
senha = ['admim', 'usuario']


def menu():
    print('***** Menu do Sistema ***** \n')
    print('    1  Criar usuário')
    print('    2  Listar usuário')
    print('    3  Atualizar usuário')
    print('    4  Deletar usuário')
    type = int(input('\nSelecione: '))
    while 1 <= type <= 4:
        if type == 1:
            create()

        elif type == 2:
            read()

        elif type == 3:
            update()

        elif type == 4:
            delete()

    else:
        print('Numero nao identificado voltando ao menu!')
        menu()


def create():
    print('\nCriar usuario!')
    id = int(input('    Insira o ID:'))
    if id in ids:
        print('ID ja existente voltando ao menu!')
        menu()
    else:
        nomes = input('    Insira o nome: ')
        senhas = input('    Insira a senha: ')
        ids.append(id)
        nome.append(nomes)
        senha.append(senhas)
        print('Usuario criado')
        print('\n1    Continuar criando')
        print('2    sair para o menu')
        type = int(input('\nSelecione:'))
        if type == 1:
            create()
        elif type == 2:
            menu()
        else:
            print('Numero nao identificado voltando ao menu!')
            menu()


def read():
    print('\nUsuarios cadastrados:\n')
    print(sorted(ids))
    id = int(input('\nPor qual ID deseja buscar?: '))
    if id in ids:
        index = ids.index(id)
        print('    ID do usuário:', ids[index])
        print('    Nome do usuário:', nome[index])
        print('    Senha do usuário:', senha[index])
    else:
        print('ID nao identificado voltando ao menu!')
        menu()
    print('Usuario listado!')
    print('\n1    Continuar listando')
    print('2    sair para o menu')
    type = int(input('\nSelecione: '))
    if type == 1:
        read()
    elif type == 2:
        menu()
    else:
        print('\nNumero nao identificado voltando ao menu!')
        menu()


def update():
    print('\nUsuarios cadastrados:\n')
    print(sorted(ids))
    id = int(input('\nDigite o ID do usuário que deseja atualizar: '))
    if id in ids:
        index = ids.index(id)
        nomes = input('    Insira o nome: ')
        senhas = input('    Insira a senha: ')
        nome.pop(index)
        senha.pop(index)
        nome.insert(id - 1, nomes)
        senha.insert(id - 1, senhas)
        print('Usuario alterado com sucesso!')
        print('\n1    Continuar alterando')
        print('2    Sair para o menu')
        type = int(input('\nSelecione:'))
        if type == 1:
            update()
        elif type == 2:
            menu()
        else:
            print('\nNumero nao identificado voltando ao menu!')
            menu()
        menu()
    else:
        print('ID nao identificado voltando ao menu!')
        menu()


def delete():
    print('\nUsuarios cadastrados:\n')
    print(sorted(ids))
    id = int(input('\nDigite o ID do usuário que deseja excluir: '))
    if id in ids:
        index = ids.index(id)
        print('\n    ID: ', ids[index], '\n    Nome: ', nome[index], '\n    Senha: ', senha[index])
        type = int(input('\nDeseja mesmo excluir este usuario? \n1    Sim\n2    Nao\nSelecione: '))
        if type == 1:
            ids.pop(index)
            nome.pop(index)
            senha.pop(index)
            print('Deletado com sucesso!')
            print('\n1    Continuar deletando')
            print('2    Sair para o menu')
            type = int(input('Selecione: '))
            if type == 1:
                delete()
            elif type == 2:
                menu()
            else:
                print('Numero nao identificado voltando ao menu!')
                menu()
        elif type == 2:
            print('Operacao cancelada!')
            print('\n1    Continuar deletando')
            print('2    Sair para o menu')
            type = int(input('Selecione: '))
            if type == 1:
                delete()
            elif type == 2:
                menu()
            else:
                print('Numero nao identificado voltando ao menu!')
                menu()
        else:
            print('Numero nao identificado voltando ao menu!')
            menu()
    else:
        print('\nID nao identificado voltando ao menu!')
        menu()

menu()