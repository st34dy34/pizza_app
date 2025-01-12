from models.order import Order
from models.pizza import PizzaFactory
from views.order_menu import OrderMenu
from utils.file_manager import FileManager
from models.observers import OrderNotifier

class OrderController:
    def __init__(self):
        self.current_order = None  # Initialize as None
        self.file_manager = FileManager()

    def create_new_order(self):
        """Create a new order if none exists"""
        self.current_order = Order()
        notifier = OrderNotifier()
        self.current_order.add_observer(notifier)

    def handle_order(self):
        if self.current_order is None or self.current_order.payment_status:
            self.create_new_order()

        order_menu = OrderMenu()
        while True:
            choice = order_menu.display_menu()
            
            if choice == "Back":
                if self.current_order.pizzas:
                    print("\nOrder Summary:")
                    for pizza in self.current_order.pizzas:
                        print(f" - {pizza.get_description()} (${pizza.get_cost():.2f})")
                    print(f"Total: ${self.current_order.get_total():.2f}")
                return

            try:
                if choice == "Custom":
                    pizza = order_menu.create_custom_pizza()
                else:
                    pizza = PizzaFactory.create_pizza(choice)
                
                self.current_order.add_pizza(pizza)
                print(f"\nAdded {pizza.get_description()} to your order.")
                
                # Save order after each modification
                self.file_manager.save_order(self.current_order, f"order_{id(self.current_order)}")
            except ValueError as e:
                print(f"\nError: {e}")