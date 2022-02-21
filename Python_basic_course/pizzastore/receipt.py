from datetime import datetime, date, time
from receipt_str import ReceiptString
import random


class Receipt(ReceiptString):
    receipt_number: int

    def __init__(self):
        super().__init__()
        self.date = date
        self.time = time
        self.receipt_number = 0
        self.list = []
        self.receiptlist = []
        self.totalsum = 0

    def __str__(self) -> str:
        return f'{self.receipt_number}, {self.receiptlist}, {self.totalsum}, {datetime.now().strftime("%H:%M")}' \
               f' {datetime.now().strftime("%d-%m-%y")}'

    def full_receipt(self) -> tuple:
        self.receipt_number += 1
        self.receiptlist = []
        self.totalsum = 0
        string_amount = random.randrange(1, 5)
        while string_amount > 0:
            self.receiptlist.append(self.receiptline())
            string_amount -= 1
        for item in self.receiptlist:
            self.totalsum += int(item[3])
        self.receipt = self.receipt_number, self.receiptlist, self.totalsum, \
                       datetime.now().strftime("%H:%M"), datetime.now().strftime("%d-%m-%y")
        return self.receipt

    def receipt_printer(self):
        print('\n', "-------YOUR ORDER-------".center(35))
        print(40 * '-')
        print(f'        Receipt number  {self.receipt_number}')
        for item in self.receiptlist:
            print(f'{item[0]:14} {item[1]} UAH X {item[2]} pcs = {item[3]} UAH')
        print(40 * '-')
        print(f'TOTAL SUM FOR RECEIPT:         {self.totalsum} UAH')
        print(f'NOW IS {datetime.now().strftime("%H:%M"):23} {datetime.now().strftime("%d-%m-%y")}')
        print(40 * '-')
