from database import connection
from functions import *
from UI import *
try:
    conn = connection()
    color(32,1)
    print('Conexão bem-sucedida!')
    color()
except:
    color(31, 1)
    print('Erro ao conectar ao banco de dados.')
    color()
    raise

cursor = conn.cursor()
while True:
    choice = menu()

    if choice == 1:
        #Create (inserting product)
        head('Inserir produto', 32, 1)
        name = validation('Nome do produto: ')
        price = validation('Preço do produto: ', 'float')
        stock = validation('Estoque do produto: ', 'int')
        afirmation = validation('Tem certeza que deseja inserir este produto? (s/n) ', 'bool')
        if afirmation:
            try:
                insert_product(cursor, name, price, stock)
                conn.commit()
                color(32, 1)
                print('Produto inserido com sucesso!')
                color()
            except Exception as e:
                color(31, 1)
                print(f'Erro ao inserir produto: {e}')
                color()
                conn.rollback()

    elif choice == 2:
        #Read (Reading Products)
        head('Ver Produto(s)', 36, 1)
        print('1 - Ver todos os produtos')
        print('2 - filtrar produtos')
        choice = validation('Escolha uma opção: ', 'int')
        if choice == 1:
            read_product(cursor, 1)
        elif choice == 2:
            #Filter (filtering Products)
            row(30)
            print('Para filtrar os produtos Digite um valor mínimo até um valor máximo')
            print('Exemplo: De-Até')
            text = '(deixe em branco para não filtrar): '
            row(30)
            print('Digite o ID Min e Máx, Exemplo: 5-20')

            filter_id = validation(text)
            row(30)
            print('Digite um caractere Min e Máx, exemplo: e-g')
            print('Ou algum conjunto de letras específico, exemplo: produto x')
            filter_name = validation(text)
            row(30)
            print('Preço Min e Max, Exemplo: 5,50-10,99')
            filter_price = validation(text)
            row(30)
            print('Estoque Min e Max, Exemplo: 100-200')
            filter_stock = validation(text)
            row(30)
            print('Data de criação Min e Max, Exemplo: 2019/01/01-2021/01/01')
            filter_date = validation(text)
            row(30)

            read_product(cursor, 2,filter_id, filter_name, filter_price, filter_stock, filter_date)

        else:
            color(31, 1)
            print('Opção inválida. Tente novamente!')
            color()

    elif choice == 3:
        #Update (updating product)
        head('Atualizar Produto', 34, 1)
        while True:
            name_or_id = validation('Nome ou ID do produto a ser atualizado: ')
            if name_or_id != '':
                break
            print('Por favor digite o nome ou ID do produto')
        new_id = validation('Novo id do produto (deixe em branco para não alterar): ', 'int', True)
        new_name = validation('Novo nome do produto (deixe em branco para não alterar): ')
        new_price = validation('Novo preço do produto (deixe em branco para não alterar): ', 'float', True)
        new_stock = validation('Novo estoque do produto (deixe em branco para não alterar): ', 'int', True)
        print('Os dados são:')
        row(30)
        print(f'Nome ou ID do produto: {name_or_id}')
        if new_name == '':
            new_name = None
        datas = [new_id, new_name, new_price, new_stock]
        msgs = [
            f'Novo id: {new_id}',
            f'Novo nome: {new_name}',
            f'Novo preço: {new_price}',
            f'Novo estoque: {new_stock}'
        ]
        for c in range(len(msgs)):
            if datas[c] is None:
                continue
            row(30)
            print(msgs[c])
        row(30)
        afirmation = validation('Tem certeza de que deseja atualizar? (s/n) ', 'bool')
        if afirmation:
            try:
                update_product(cursor, name_or_id, new_id, new_name, new_price, new_stock)
                not_found(cursor)
                conn.commit()
                color(32, 1)
                print('Produto atualizado com sucesso!')
                color()
            except Exception as e:
                color(31, 1)
                print(f'Erro ao atualizar produto: {e}')
                color()
                conn.rollback()

    elif choice == 4:
        #Delete (deleting product)
        head('Deletar Produto', 31, 1)
        name_or_id = validation('Nome ou ID do produto a ser deletado: ')
        afirmation = validation('Tem certeza que deseja deletar este produto? (s/n) ', 'bool')
        if afirmation:
            try:
                delete_product(cursor, name_or_id)
                not_found(cursor)
                conn.commit()
                color(32, 1)
                print('Produto deletado com sucesso!')
                color()
                sleep(0.25)
            except Exception as e:
                color(31, 1)
                print(f'Erro ao deletar produto: {e}')
                color()
                conn.rollback()


    elif choice == 5:
        color(33)
        print('saindo...')
        color()
        sleep(0.5)
        break
    else:
        color(31,1)
        print('Opção inválida. Tente novamente!')
        color()
