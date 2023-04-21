# Super-Cashier-Apps

## Introductory
This is a Python-based shopping cart application that allows users to add items, modify their information, and proceed to checkout. The application is designed to be simple to use, allowing users to quickly and easily add and manage items in their shopping cart.

## Objective/Requirement
The objective of this project is to create a simple and functional shopping cart application that allows users to:

- The ability to add and remove items from the cart
- The ability to modify item quantity
- The ability to store user information such as name and address
- The ability to calculate total cost including tax and shipping
- The ability to connect to a PostgreSQL database to store transaction data

For teh requirment, this project use:
- Python 
  - tabulate module
  - psycopg2 module
- PostgreSQL

## Program Description
The project consists of two main files: a modular file and a main file. The modular file contains the functions and classes required for the shopping cart application, while the main file calls these functions to run the application.
The function in modulare file are:
- add_item(): 
- update_item_name():
- update_item_qty():
- update_item_price():
- delete_item()
- reset_transaction():
- check_order():
- check_out():

While in main file is contains the main program logic for the shopping cart application. It consists of a main menu where users can select options to add items, update items, view the cart, and checkout. 
The Shopping Cart Application uses PostgreSQL as the database management system to store transaction data. It consists of one table named "transactions," which stores the details of each transaction made by the user.

## Test Case
Testing is an essential part of software development as it ensures the program works as intended and helps catch and fix bugs before release. In this project, we have included test cases to ensure the shopping cart application's functionality is working correctly. The test cases cover all the critical functions, such as adding items, updating their details, and checking out. 

- Add item

![add item case](https://user-images.githubusercontent.com/122255417/233657188-66a08a4d-98ff-4cf1-8df1-86a77471b822.png)

- update item quantity

![update quantity case](https://user-images.githubusercontent.com/122255417/233657578-76af23d7-52a8-47c9-9e05-837813141a89.png)
- check order

![check order](https://user-images.githubusercontent.com/122255417/233657377-bd641374-9557-4f2e-9fe6-605097cc421a.png)
- check out

![check out](https://user-images.githubusercontent.com/122255417/233657464-62455f0b-096a-445f-8cdd-38345917a658.png)

- data sucessfully stored in postgresql

![psql database](https://user-images.githubusercontent.com/122255417/233658313-4ae46760-49e5-42b3-b77b-c3f4464a2a30.png)









