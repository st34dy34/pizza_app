# models/pizza.py
from abc import ABC, abstractmethod

class PizzaComponent(ABC):
    @abstractmethod
    def get_cost(self):
        pass

    @abstractmethod
    def get_description(self):
        pass

# --- CUSTOM PIZZAS  SECTION----
class BasePizza(PizzaComponent):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def get_cost(self):
        return 0.0

    def get_description(self):
        return f"{self.size} {self.name} Pizza"

class PizzaDecorator(PizzaComponent):
    def __init__(self, pizza: PizzaComponent):
        self.pizza = pizza

    def get_cost(self):
        return self.pizza.get_cost()

    def get_description(self):
        return self.pizza.get_description()

class ToppingDecorator(PizzaDecorator):
    def __init__(self, pizza: PizzaComponent, topping_name: str, topping_price: float):
        super().__init__(pizza)
        self.topping_name = topping_name
        self.topping_price = topping_price

    def get_cost(self):
        return super().get_cost() + self.topping_price

    def get_description(self):
        return f"{super().get_description()} with {self.topping_name}"

# --- PREMADE PIZZAS SECTION----
class Pepperoni(BasePizza):
    def __init__(self):
        super().__init__("Pepperoni", "Medium")
    
    def get_cost(self):
        return 10.00

class Chilli(BasePizza):
    def __init__(self):
        super().__init__("Chilli", "Large")
    
    def get_cost(self):
        return 12.00

# --- FACTORY PATTERN ---
class PizzaFactory:
    @staticmethod
    def create_pizza(pizza_type: str) -> PizzaComponent:
        if pizza_type == "Pepperoni":
            return Pepperoni()
        elif pizza_type == "Chilli":
            return Chilli()
        elif pizza_type == "Custom":
            return BasePizza("Custom", "Medium")
        else:
            raise ValueError(f"Unknown pizza type: {pizza_type}")