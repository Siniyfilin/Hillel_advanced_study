import os
import sqlite3

from typing import List, Tuple


def execute_query(query_sql: str) -> List:
    '''
    Функция для выполнения запроса
    :param query_sql: запрос
    :return: результат выполнения запроса
    '''
    db_pass = os.path.join(os.getcwd(), 'chinook.db')
    connection = sqlite3.connect(db_pass)
    cur = connection.cursor()
    result = cur.execute(query_sql)
    return result


def values_summation(records: List) -> float:
    '''
    Функция которая возвращает сумму значний
    :param records:  список значений из БД
    :return: значение суммы
    '''
    sum_of_values = sum([float(item[0]) for item in records])
    return sum_of_values


def get_units_list() -> Tuple:
    '''
    Возвращает списки значений колонок UnitPrice и Quantity из таблицы invoice_items
    '''
    unitprice_sql = f'''
        SELECT UnitPrice
          FROM invoice_items
    '''
    unit_quantity_sql = f'''
        SELECT Quantity
          FROM invoice_items
    '''
    return values_summation(execute_query(unitprice_sql)), values_summation(execute_query(unit_quantity_sql))


def main_function():
    '''
    Функция выводит результат умножения сумм колонок UnitPrice и Quantity из таблицы invoice_items
    '''
    var = get_units_list()
    print(f'Прибыль составляет: {var[0] * var[1]:.2f} ед.')


main_function()
