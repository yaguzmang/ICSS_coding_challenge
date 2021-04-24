"""Run script. This script runs a solution to the ICSS challenge 2021."""

__author__      = "Yhoan Alejandro Guzmán García"
__version__     = "1.0"
__email__ = "yaguzmang@eafit.edu.co"

import helpers 
from trie.trie import Trie

def run():
    print("")
    print("**** Coding challenge ****")
    input_option = helpers.get_input_option() #1 for manual, 2 for reading the example telephone prefixes
    trie = Trie()
    if input_option == 1: 
        operators_data = helpers.get_input_data()
    elif input_option == 2:
        operators_data = helpers.read_input_data()
    
    print("Saving telephone prefixes...")
    print("")
    for operator in operators_data.keys():
        for item in operators_data[operator]:
            telephone_prefix = item[0]
            price = item[1]
            operator_name = str(operator)
            trie.insert(operator_name,telephone_prefix,price)
    print("Prices: ")
    helpers.pprint_operators(operators_data)
    print("")
    print("Input a telephone number to find its cheapest operator or 'exit' to exit the program")
    while True:
        number = str(input("Find cheapest for: "))
        if number.lower() == 'exit':
            break
        elif helpers.is_phone_valid(number):
                cheapest_option = trie.find_cheapest(number)
                operator = cheapest_option[2]
                if operator is None:
                    print("No operator supports that telephone number")
                    continue
                prefix = cheapest_option[1]
                price = cheapest_option[0]
                print(f"Cheapest operator: Operator {operator}")
                print('prefix: {0:8}  price: {1}/min'.format(prefix, price))
        else:
            print("Please input a valid telephone number or 'exit' to exit the program")

    print("Exiting...")
    print("")
if __name__ == '__main__':
    run()