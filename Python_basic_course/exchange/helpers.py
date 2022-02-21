import csv
import requests


def reader_from_api():
    url = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
    req = requests.get(url)
    data = req.json()
    return data


def reader_from_data_storage():
    data_from_file = {}
    with open('datastorage.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data_from_file.update(row)
        return data_from_file


def initialization():
    temp_dict_storage = reader_from_data_storage()
    temp_dict_api = reader_from_api()
    temp_dict_storage.update(USD_current_rate=(temp_dict_api[0].get('sale')),
                             UAH_current_rate=temp_dict_api[0].get('buy'))
    writer_to_data_storage(temp_dict_storage)
    print('Greetings! The current exchange rate has been updated.')


def writer_to_data_storage(temp_dict):
    with open('datastorage.csv', 'w', newline='') as csvfile:
        fieldnames = ["USD_current_rate", "UAH_current_rate", "USD", "UAH"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(temp_dict)


def refresh_balance(result, input_var, input_string):
    temp_dict_storage = reader_from_data_storage()
    if input_string == 'USD':
        dollars = round(float(temp_dict_storage.get('USD')) - float(input_var), 2)
        hrivnas = round(float(temp_dict_storage.get('UAH')) + float(result), 2)
    else:
        dollars = round(float(temp_dict_storage.get('USD')) + float(result), 2)
        hrivnas = round(float(temp_dict_storage.get('UAH')) - float(input_var), 2)
    temp_dict_storage.update(USD=dollars, UAH=hrivnas)
    writer_to_data_storage(temp_dict_storage)


def exchange(input_var, input_string):
    if input_var <= float(reader_from_data_storage().get(input_string)):
        if input_string == 'USD':
            result = round(input_var * float(reader_from_data_storage().get('USD_current_rate')), 2)
            refresh_balance(result, input_var, input_string)
            print(f'UAH {result}, RATE {reader_from_data_storage().get("USD_current_rate")}')
        else:
            result = round(input_var / float(reader_from_data_storage().get('UAH_current_rate')), 2)
            refresh_balance(result, input_var, input_string)
            print(f'USD {result}, RATE {1 / float(reader_from_data_storage().get("UAH_current_rate")):.6f}')
    else:
        print('Insufficient funds in the treasury')
