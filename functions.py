from time import sleep

def replaces(dictionary):
    for k, v in list(dictionary.items()):
        if v == '' or v is None:
            dictionary.pop(k, None)
        else:
            v = (v.replace(' ', '').replace(',', '.')).split('-')
            if '/' in dictionary[k]:
                v[0] = v[0].replace('/', '-')
                v[1] = v[1].replace('/', '-')
            dictionary[k] = v
    return dictionary


def insert_product(cursor, name, price, stock):
    cursor.execute("INSERT INTO products (name, price, stock) VALUES (%s, %s, %s)",
        (name, price, stock)
    )


def read_product(cursor, choice=1, filter_id=None, filter_name=None, filter_price=None, filter_stock=None, filter_date=None):

    if choice == 1:
        cursor.execute("SELECT id, name, price, stock, created_at FROM products")
    else:
        filters = replaces(dictionary = {
            'id': filter_id,
            'name': filter_name,
            'price': filter_price,
            'stock': filter_stock,
            'created_at': filter_date
        })
        set_clauses = []
        for k, v in filters.items():
            if len(v) == 2:
                for condition in v:
                    if v[0] == condition:
                        clause = f'{k} >= %s'

                    else:
                        clause = f'{k} <= %s'
                    set_clauses.append(clause)
            else:
                set_clauses.append(f'{k} = %s')

        values = [value for lists in filters.values() for value in lists]

        query = f"SELECT id, name, price, stock, created_at FROM products WHERE {' AND '.join(set_clauses)}"
        cursor.execute(query, (*values,))

    rows = cursor.fetchall()
    print(f'{"id":<5} {"name":<15} {"price":>10} {"stock":>10} {"created_at":>15}')
    print('-'*70)
    for row in rows:
        sleep(0.25)
        print(f'{row[0]:<5} {row[1]:<15} {row[2]:>10} {row[3]:>10} {(row[4].strftime("%d/%m/%Y %H:%M:%S")):>25}')
    print('-' * 70)
    sleep(1)


def update_product(cursor, name_or_id, new_id=None, new_name=None, new_price=None, new_stock=None):
    if name_or_id.isnumeric():
        identifier = "id"
    else:
        identifier = "name"

    updates = [
        ("id = %s", new_id) , ("name = %s", new_name),
        ("price = %s", new_price), ("stock = %s", new_stock)
    ]

    values = []
    set_clauses = []

    for clause, value in updates:
        if value is not None:
            set_clauses.append(clause)
            values.append(value)

    query = f"UPDATE products SET {', '.join(set_clauses)} WHERE {identifier} = %s"

    return cursor.execute(query, (*values, name_or_id))


def delete_product(cursor, name_or_id):
    if name_or_id.isnumeric():
        cursor.execute("DELETE FROM products WHERE id = %s", (name_or_id,))
    else:
        cursor.execute("DELETE FROM products WHERE name = %s", (name_or_id,))
