

class Pizza:

    def __init__(self, pizza_idx, pizza_name, pizza_price, pizza_ingridients):
        self.idx = pizza_idx
        self.name = pizza_name
        self.price = pizza_price
        self.ingridients = pizza_ingridients

    def __str__(self) -> str:
        return f'{self.idx}, {self.name}, {self.price}, {self.ingridients}'

    def getpizza(self) -> tuple:
        return self.idx, self.name, self.price, self.ingridients
