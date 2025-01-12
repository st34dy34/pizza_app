class Order:
    def __init__(self):
        self.pizzas = []
        self.payment_status = False
        self.total_price = 0.0
        self.observers = []
        self.status = "Created"

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.status)

    def set_status(self, status: str):
        self.status = status
        self.notify_observers()

    def add_pizza(self, pizza):
        self.pizzas.append(pizza)
        self.total_price += pizza.get_cost()
        self.set_status("Updated")

    def get_total(self):  # New method that returns total_price
        return self.total_price

    def set_payment_status(self, status: bool):
        self.payment_status = status
        self.set_status("Paid" if status else "Payment Failed")

    def __str__(self):
        pizza_list = "\n".join([f"- {pizza.get_description()}" for pizza in self.pizzas])
        return f"Order:\n{pizza_list}\nTotal: ${self.total_price:.2f}\nPaid: {self.payment_status}"
