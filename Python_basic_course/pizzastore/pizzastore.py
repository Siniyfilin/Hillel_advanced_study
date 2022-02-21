
from helpers import printing_table, printing_main_menu, add_new_pizza, reader
from receipt import Receipt

print(109 * "-")
print('*****We are happy to see you in our pizza cafe*****'.center(109))
print(109 * "-")

pizzamenu = reader()

class SingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class PizzaStore(metaclass=SingletonMeta):
    def __init__(self):
        self.receipts = []

    def main_menu(self):
        while True:
            printing_main_menu()  # from helpers.py
            choice = (input('Enter your choice: '))
            match choice:
                case '0':  # exit from program
                    print(26 * '-')
                    print('Good bye. Have a nice day')
                    print(26 * '-')
                    break
                case '1':  # printing menu table from pizza.py
                    printing_table(pizzamenu)
                case '2':  # random_choice_pizza from helpers.py
                    temp = Receipt()
                    self.receipts.append(temp.full_receipt())
                    temp.receipt_printer()
                case '3':  # filtering from helpers.py
                    try:
                        condition = int(input('Please enter max price for pizza(from 144 to 999):'))
                        filter_list = [item for item in pizzamenu if int(item[2]) <= condition]
                        if len(filter_list) > 0:
                            print(f'PIZZAS THAT COST NO MORE THAN {condition} UAH'.center(109))
                            printing_table(filter_list)
                        else:
                            print('\n***we don\'t have such pizzas***\n')
                    except Exception:
                        print(40 * '-')
                        print('Incorrect input, try again')
                        print(40 * '-')
                case '4':  # adding new pizza
                    add_new_pizza()
                case '5':
                    for item in self.receipts:
                        print(40 * '-')
                        print(f'receipt number {item[0]} from {item[4]} {item[3]}')
                        for elem in item[1]:
                            print(f'{elem[0]:14} {elem[1]} UAH X {elem[2]} = {elem[3]}')
                        print(40 * '-')
                        print(f' with total cost {item[2]} UAH')
                        print(40 * '-')
                case _:
                    print('Invalid choice\n')


magaz = PizzaStore()
magaz.main_menu()
