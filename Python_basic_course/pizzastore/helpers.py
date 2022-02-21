from datetime import datetime
import csv
from pizza import Pizza
from os.path import exists


def reader():
    pizzamenu = []
    if exists('names.csv'):
        with open('names.csv', newline='') as csvfile:
            readerin = csv.DictReader(csvfile)
            for row in readerin:
                pizza = Pizza(row['idx'], row['name'], row['price'], row['ingridients'])
                pizzamenu.append(pizza.getpizza())
            return pizzamenu
    else:
        pizzamenu = []
        return pizzamenu


def printing_table(some_list):  # printing menu table
    print('_' * 109)  # begin
    print(f'|code | {"Name":15} | {"Price":7} | {"Description":71} |')
    print('_' * 109)
    for item in some_list:  # printing strings of table
        print(f'| {item[0]:3} | {item[1]:15} | {item[2]} UAH | {item[3]:72}|')
    print('_' * 109)


def add_new_pizza():
    temp_dict = {'idx': None, 'name': None, 'price': None, 'ingridients': None}
    for k in temp_dict.keys():
        item = input(f'Please enter {k}: ')
        temp_dict[k] = item
    with open('names.csv', 'at') as csvfile:
        fieldnames = ['idx', 'name', 'price', 'ingridients']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(temp_dict)


def decorator(function_for_decor):  # decorated printing_main_menu by adding current time and date
    def new_view():
        function_for_decor()
        current_datetime = datetime.now()
        print(26 * '-')
        print("We work from 8 am to 8 pm")
        print(f'Now is {current_datetime.strftime("%H:%M")} {current_datetime.strftime("%d-%m-%y")}')
        print(26 * '-')
    return new_view


@decorator
def printing_main_menu():
    print('---MAIN MENU---\n'
          '1: print menu.\n'
          '2: add to cart.\n'
          '3: filter by price.\n'
          '4: add new pizza.\n'
          '5: printing receipts.\n'
          '0: exit from our pizza store.')
