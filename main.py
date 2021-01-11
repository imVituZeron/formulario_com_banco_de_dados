from db.querys import insert, list_data, delete

while True:
    print('Welcome to Vitor´s databases')
    print(
        """
        1 -  Create registration
        2 -  Update data
        3 -  List data
        4 -  Delete registration
        5 -  Exit
        """
        )
    op = int(input("Qual das opções acima voce escolheu? "))
    if op == 1:
        name = str(input('Digite seu nome: '))
        age = int(input('Digite sua idade: '))
        mail = str(input('Digite seu email: '))
        phone = str(input('Digite seu telephone (99999999): '))
        if insert(name, age, mail, phone):
            print('Criado o cadastro com sucesso!')
        else:
            print('Ocorreu um erro!')

    elif op == 4:
        print('=-='* 10)
        ident = int(input('Digite o numero de identificação do cadastro que deseja deletar: '))
        if delete(ident):
            print('Exclusão feita com sucesso!')
        else:
            print('Ocorreu um erro!')

    elif op == 3:
        print('=-='* 10)
        list_data()

    elif op == 5:
        print('=-='* 10)
        print('Obrigado pela visita')
        break

