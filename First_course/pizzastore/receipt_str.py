
from helpers import reader
import random


class ReceiptString:
    @staticmethod
    def receiptline():
        random_amount_in_string = random.randrange(1, 5)
        temp_var = random.choice(reader())
        string_sum = random_amount_in_string * int(temp_var[2])
        return temp_var[1], temp_var[2], random_amount_in_string, string_sum
