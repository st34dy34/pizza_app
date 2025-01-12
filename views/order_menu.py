from models.pizza import BasePizza, ToppingDecorator

class OrderMenu:
    @staticmethod
    def display_menu():
        print("\n--- Order Menu ---")
        print("1. Pepperoni Pizza (10 USD)")
        print("2. Chilli Pizza (12 USD)")
        print("3. Custom Pizza")
        print("4. Back")
        
        while True:
            choice = input("Choose an option (1-4): ").strip()
            
            if choice == "1":
                return "Pepperoni"
            elif choice == "2":
                return "Chilli"
            elif choice == "3":
                return "Custom"
            elif choice == "4":
                return "Back"
            else:
                print("Invalid choice. Please try again.")

    @staticmethod
    def create_custom_pizza():
        base_pizza = BasePizza("Custom", "Medium")
        pizza = base_pizza

        available_toppings = {
            "Cheese": 2.0,
            "Mushrooms": 1.5,
            "Olives": 1.0,
            "Pepperoni": 2.5,
            "Chicken": 3.0
        }

        print("\nAvailable toppings:")
        for topping, price in available_toppings.items():
            print(f"- {topping} (${price:.2f})")

        while True:
            topping = input("\nAdd topping (or 'done' to finish): ").strip().title()
            if topping.lower() == 'done':
                break
            
            if topping in available_toppings:
                pizza = ToppingDecorator(pizza, topping, available_toppings[topping])
                print(f"Added {topping}")
            else:
                print("Invalid topping. Please try again.")

        return pizza