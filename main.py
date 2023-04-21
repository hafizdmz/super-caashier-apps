from function import *


def main():
    main_menu()


def main_menu():
    while True:
        if len(transaction_dict) == 0:
            print(f'1. Add item to basket')
        else:
            print(
                '''
    1. Add item to basket
    2. Update or modify item name in basket
    3. Update of modify quantity in basket
    4. Update or modify price in basket
    5. Delete item in basket
    6. Clear all items in basket
    7. Proceed to checkout    
                ''')

        user_input = int(
            input(f'Please select an option from the menu above by entering the corresponding number: '))

        if user_input == 1:
            while True:
                add_item()
                while True:
                    input_repeat = input(f'Do you want to add more item to your basket? (y/n): ')
                    if input_repeat == 'y':
                        break
                    elif input_repeat == 'n':
                        break
                    else:
                        print(f"Invalid input. Please answer with letter 'y' or 'n'.")
                if input_repeat == 'n':
                    break

        elif user_input == 2 and len(transaction_dict) != 0:
            while True:
                update_item_name()
                while True:
                    input_repeat = input(f'Do you want to update more item name in your basket? (y/n): ')
                    if input_repeat == 'y':
                        break
                    elif input_repeat == 'n':
                        break
                    else:
                        print(f"Invalid input. Please answer with letter 'y' or 'n'.")
                if input_repeat == 'n':
                    break

        elif user_input == 3 and len(transaction_dict) != 0:
            while True:
                update_item_qty()
                while True:
                    input_repeat = input(f'Do you want to update more item quantity in your basket? (y/n): ')
                    if input_repeat == 'y':
                        break
                    elif input_repeat == 'n':
                        break
                    else:
                        print(f"Invalid input. Please answer with letter 'y' or 'n'.")
                if input_repeat == 'n':
                    break

        elif user_input == 4 and len(transaction_dict) != 0:
            while True:
                update_item_price()
                while True:
                    input_repeat = input(f'Do you want to update more item price in your basket? (y/n): ')
                    if input_repeat == 'y':
                        break
                    elif input_repeat == 'n':
                        break
                    else:
                        print(f"Invalid input. Please answer with letter 'y' or 'n'.")
                if input_repeat == 'n':
                    break

        elif user_input == 5 and len(transaction_dict) != 0:
            while True:
                delete_item()
                while True:
                    input_repeat = input(f'Do you want to delete more item in your basket? (y/n): ')
                    if input_repeat == 'y':
                        break
                    elif input_repeat == 'n':
                        break
                    else:
                        print(f"Invalid input. Please answer with letter 'y' or 'n'.")
                if input_repeat == 'n':
                    break

        elif user_input == 6 and len(transaction_dict) != 0:
            while True:
                input_confirmation = input(f'Are you sure want to clear all transaction? (y/n) ')
                if input_confirmation == 'y':
                    reset_transaction()
                    print(f'All items in the basket have been cleared.')
                    break
                elif input_confirmation == 'n':
                    break
                else:
                    print(f"Invalid input. Please answer with letter 'y' or 'n'.")

        elif user_input == 7 and len(transaction_dict) != 0:
            while True:
                check_order()
                input_proceed = input(f'Continue to checkout the basket or back to main menu? (y/n) ')
                if input_proceed == 'y':
                    check_out()
                    break
                elif input_proceed == 'n':
                    break
                else:
                    print(f"Invalid input. Please answer with letter 'y' or 'n'.")
            if input_proceed == 'y':
                break

        else:
            print(f'Input invalid. Please enter number based on menu available.')


if __name__ == "__main__":
    main()
