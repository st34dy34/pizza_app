class Topping:
    def __init__(self, name, extra_price):
        self.name = name
        self.extra_price = extra_price

    def __str__(self):
        return f"Topping: {self.name} (${self.extra_price})"