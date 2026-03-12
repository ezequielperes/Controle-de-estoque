from time import sleep


def not_found(cursor):
    if cursor.rowcount == 0:
        color(33,1)
        raise Exception ('Produto não encontrado!')

def validation(input_text, expected_type='str', avoid_changes=False):
    value = None
    while True:
        try:
            if avoid_changes and expected_type in ['int', 'float', 'str']:
                value = input(input_text)
                if value == '':
                    value = None
                    return value
                else:
                    if expected_type == 'int':
                        value = int(value)
                    else:
                        value = float(value.replace(',', '.'))

            elif expected_type == 'float':
                value = float(input(input_text).replace(',', '.'))

            elif expected_type == 'bool':
                while True:
                        value = input(input_text).lower().strip()
                        if value in ['y', 's']:
                            value = True
                            break
                        elif value == 'n':
                            value = False
                            break
                        else:
                            color(31,1)
                            print(f'Entrada inválida!')
                            color()
            elif expected_type == 'int':
                value = int(input(input_text))
            elif expected_type == 'str':
                value = input(input_text)
            return value
        except (ValueError, TypeError, KeyboardInterrupt):
            color(31,1)
            print(f'Entrada inválida!')
            color()


def row(size):
    print('-'*size)


def head(text, number_color=0, number_format=0):
    color(number_format,number_color)
    row(len(text)+4)
    sleep(0.2)
    print(text.center(len(text)+4))
    sleep(0.2)
    row(len(text)+4)
    color()


def color(number_color=0, number_format=0):
    print(f'\033[{number_format};{number_color}m', end='')


def menu():
    sleep(0.5)
    head('MENU'.center(30),35,1)
    color(32,1)
    print('1 - Inserir produto')
    sleep(0.25)
    color(36,1)
    print('2 - Ver produto(s)')
    sleep(0.25)
    color(34, 1)
    print('3 - Atualizar produto')
    sleep(0.25)
    color(31, 1)
    print('4 - Deletar produto')
    sleep(0.25)
    color(33, 1)
    print('5 - Sair')
    sleep(0.25)
    color()
    choice = validation('Escolha uma opção: ', 'int')
    return choice
