from tabulate import tabulate
import psycopg2

transaction_dict = {}
table = []


def print_separator(func):
    def wrapper(*args, **kwargs):
        print("------------")
        result = func(*args, **kwargs)
        print("------------")
        return result

    return wrapper


@print_separator
def add_item():
    """
    Adds an item to a basket with user-provided input for name, quantity, and price.
    """
    try:
        input_name = input(f'Please enter the name of item: ')
        input_qty = int(input(f'Please enter the quantity of item: '))
        input_price = int(input(f'Please enter the price of item: '))
    except ValueError:
        print("Error: Quantity and price must be a number")
        return

    if input_qty <= 0 or input_price <= 0:
        print("Error: Quantity and price must be greater than 0")
        return

    item = {input_name: [input_qty, input_price, input_qty * input_price]}
    print(f'{item} is successfully added to basket')
    transaction_dict.update(item)


@print_separator
def update_item_name():
    """
    Modify the name of an item in the transaction basket based on user input.
    """
    print(f'Items in basket are:{list(transaction_dict.keys())}')
    input_name = input(f'Please enter the name of the item you want to update: ')
    if input_name not in transaction_dict:
        print(f'Error: Item {input_name} not found in transaction basket.')
        return
    input_update = input(f'Please enter the updated item name: ')
    transaction_dict[input_update] = transaction_dict.pop(input_name)
    print(f'Item name {input_name} is updated to {input_update}')


@print_separator
def update_item_qty():
    """
    Modify the quantity of an item in the transaction basket based on user input.
    """
    print(f'Items in basket are:{list(transaction_dict.keys())}')
    input_name = input(f'Please enter the name of the item you want to update: ')
    try:
        transaction_dict[input_name]
    except KeyError:
        print(f'Error: Item name {input_name} not found in transaction basket')
        return
    try:
        input_update = int(input(f'Please enter the updated item quantity: '))
    except ValueError:
        print(f'Error: Please enter a valid value for quantity.')
        return

    transaction_dict[input_name][0] = input_update
    transaction_dict[input_name][2] = input_update * transaction_dict[input_name][1]
    print(f'{input_name} quantity has been updated to {input_update}.')


@print_separator
def update_item_price():
    """
    Modify the price of an item in the transaction basket based on user input.
    """
    print(f'Items in basket are:{list(transaction_dict.keys())}')
    input_name = input(f'Please enter the name of the item you want to update: ')
    try:
        transaction_dict[input_name]
    except KeyError:
        print(f'Error: {input_name} not found in transaction basket')
        return
    try:
        input_update = float(input(f' Please enter the updated item price: '))
    except ValueError:
        print(f'Error: Please enter a valid value for price update.')
        return
    transaction_dict[input_name][1] = input_update
    transaction_dict[input_name][2] = input_update * transaction_dict[input_name][0]


@print_separator
def delete_item():
    """
    Deletes an item from the transaction basket based on user input.
    """
    print(f'Items in basket are:{list(transaction_dict.keys())}')
    input_name = input(f'Please enter the name of the item you want to delete: ')
    try:
        transaction_dict.pop(input_name)
        print(f'Item {input_name} is successfully deleted from basket.')
    except KeyError:
        print(f'Item {input_name} not found in basket.')


@print_separator
def reset_transaction():
    """
    This function clears the transaction dictionary, removing all items added to the basket.
    """

    transaction_dict.clear()


@print_separator
def check_order():
    """
    Displays the details of all items in the transaction basket.
    """
    headers = ['Item Name', 'Quantity', 'Item Price', 'Total Price']
    for item_name, item_data in transaction_dict.items():
        item_qty, item_price, item_total = item_data
        table.append([item_name, item_qty, item_price, item_total])
    print(f'Here are all items detail in your basket:')
    print(tabulate(table, headers=headers, tablefmt='pretty'))


@print_separator
def check_out():
    """
    Calculates the total transaction price with discounts and displays the checkout details and store data into database.
    """
    conn = psycopg2.connect(
        host="localhost",
        database="super_cashier_apps",
        user="postgres",
        password="onlyme"
    )
    cur = conn.cursor()
    headers = ['Purchase Id', 'Item Name', 'Quantity', 'Price', 'Total Price', 'Discount', 'Final Price']
    checkout_list = []
    start_id = 1
    total_discount = 0
    total_pay = 0
    for item in table:
        item_name, item_qty, item_price, total_price = item
        discount = 0
        if total_price >= 500000:
            discount = 0.07
        elif total_price >= 300000:
            discount = 0.06
        elif total_price >= 200000:
            discount = 0.05
        discount_price = round(total_price * discount)
        total_discount += discount_price
        final_price = total_price - discount_price
        total_pay += final_price
        checkout_list.append([start_id, item_name, item_qty, item_price, total_price, discount_price, final_price])
        start_id += 1
    print(tabulate(checkout_list, headers=headers, tablefmt='pretty'))
    for item in checkout_list:
        cur.execute(
            "INSERT INTO transactions (trans_id, item_name, item_qty, item_price, total_price, discount, disc_price) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            item)
    conn.commit()
    cur.close()
    conn.close()
    if total_discount != 0:
        print(f'Congratulation, you save up Rp.{total_discount}. Your total transaction is now Rp.{total_pay}')
    else:
        print(f'Your total transaction is Rp.{total_pay}')
