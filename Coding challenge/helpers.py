"""Helper module for the run script

This module contains the necessary methods to allow the user manually input 
the operators data, or to read the data from the ./test/examples.txt file.
This script also contains a pretty printer method to print the operators data.

This file can be imported and contains the following functions:

    * get_input_option - returns data read option inputted by the user
    * get_input_data - returns the operators' data inputted by the user
    * get_phone_prefix - returns a valid phone prefix inputted by the user
    * get_price - returns a valid price inputted by the user
    * read_input_data - returns the operators' data located at:
                        ./test/examples.txt
    * is_phone_valid - returns whether a phone number is valid or not             
    * is_price_valid - returns whether a price is valid or not
    * is_price_valid - returns whether a price is valid or not      
    * pprint_operators - pretty prints the operators' data
"""

def get_input_option() -> int:

    while True:
        input_text = "Please input 1 if you want to write the operators prefixes and prices,\nor 2 if you want to use the existing data: "
        options = {1, 2}
        try:
            option = int(input(input_text))
        except ValueError:
            print("Please input 1 or 2 only")
            continue
        if option not in options:
            print("Please input 1 or 2 only")
            continue
        else:
            break
    return option

def get_input_data() -> dict:
    operators = {}
    op_count = 1
    print("\n **** Please input the telephone prefixes and prices **** \n")
    print("type 'continue' to continue with another operator, or 'exit' to finish")
    print("---")
    print(f"Operator {op_count}: ")
    operator_data = []
    operators[op_count] = operator_data
    
    while True:
        phone_prefix = get_phone_prefix()
        if phone_prefix == 'exit':
            break
        elif phone_prefix == 'continue':
            op_count += 1
            operator_data = []
            operators[op_count] = operator_data
            print(f"Operator {op_count}: ")
            continue
        else:
            price = get_price(phone_prefix)
        operator_data.append([phone_prefix, price])
    return operators

def get_phone_prefix() -> str:
    
    phone_prefix = None
    is_prefix_valid = False

    while not is_prefix_valid:
        phone_prefix = input("New telephone prefix: ")

        if phone_prefix == 'continue':
            return 'continue'
        elif phone_prefix == 'exit':
            return 'exit'
        elif is_phone_valid(phone_prefix):
            phone_prefix = str(phone_prefix)
            is_prefix_valid = True
        else:
            print("Please input a valid phone number or 'exit' to continue")
            continue
    return phone_prefix

def get_price(phone_prefix: str) -> float:
    
    price = None
    valid_price = False

    while not valid_price:
        price = input(f"Price for {phone_prefix}: ")
        if price == 'exit':
            print("Please set a price for the current phone prefix before exiting")
            continue
        elif is_price_valid(price):
            price = float(price)
            valid_price = True
        else:
            print("Please input a non-negative valid number")
            continue
    return price
    

def read_input_data() -> dict:
    operators = {}
    f = open("tests/example.txt")
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        data = line.split(" ")
        if data[0].lower() == "operator":
            operator_data = []
            operators[data[1]] = operator_data
        else:
            phone_prefix = data[0]
            price = data[1]
            if is_phone_valid(phone_prefix) and is_price_valid(price):
                operator_data.append([str(phone_prefix), float(price)])
            else:
                continue
    return operators

def is_phone_valid(phone_prefix: str) -> bool:
    return phone_prefix.isdigit()

def is_price_valid(price: str) -> bool:
    try:
        price = float(price)
        if price < 0:
            return False
    except ValueError:
        return False
    return True

def pprint_operators(operators_data: dict) -> None:
    for operator in operators_data.keys():
        print(f"Operator {operator}")
        for data in operators_data[operator]:
            prefix = data[0]
            price = data[1]
            print('{0:6}  {1}'.format(prefix, price))