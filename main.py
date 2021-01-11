from db.querys import insert, list_data, delete
from db.querys import update_name, update_age, update_mail, update_phone, get_date_select

while True:
    print('=-='* 10)
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

    elif op == 2:
        print('=-='* 10)
        print(
            """
            1 - nome
            2 - idade
            3 - email
            4 - telefone
            """
        )
        list_ops = ['1', '2', '3', '4']
        field_value = input('Digite o numero que corresponde com o campo que deseja modificar: ')
        
        if field_value.isdigit() and field_value in list_ops:
            identification = input('Digite o id do cadastro que deseja modificar: ')
            if identification.isdigit() and get_date_select(identification):
                value = input('Digite o valor que quer colocar no campo escolhido: ')
                if field_value == '1':
                    if update_name(value, int(identification)):
                        print('Modificação feita com sucesso!')
                    else:
                        print('Ocorreu um erro!')

                elif field_value == '2':
                    if value.isdigit():
                        if update_age(int(value), int(identification)):
                                print('Modificação feita com sucesso!')
                        else:
                            print('Ocorreu um erro!')   

                elif field_value == '3':
                    if update_mail(value, int(identification)):
                         print('Modificação feita com sucesso!')
                    else:
                        print('Ocorreu um erro!')
                    
                elif field_value == '4':
                    if update_phone(value, int(identification)):
                        print('Modificação feita com sucesso!')
                    else:
                        print('Ocorreu um erro!')
                
            else:
                print('Identificador desconhecido')
        else:
            print('Opção desconhecida') 

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

