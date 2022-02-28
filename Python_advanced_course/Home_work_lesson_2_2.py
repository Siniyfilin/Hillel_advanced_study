import os
import sqlite3

from collections import Counter
from typing import List


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


def get_units_list() -> List:
    '''
    Возвращает список значений из БД
    '''
    query_sql = f'''
        SELECT FirstName
          FROM customers
    '''
    return unwrapper(execute_query(query_sql))


def unwrapper(records: List) -> None:
    '''
    Функция выводит список повторяющихся эл-тов из колонки FirstName таблицы cutomers и количество повторений
    :param records: список ответа БД
    '''
    first_names = Counter(records)
    for k, v in first_names.items():
        if v > 1:
            print(f'Повторяющееся имя: {k[0]}, количество повторений: {v}')


get_units_list()
