class PaymentMenu:
    def display_payment_methods(self):
        print("\n--- Payment Methods ---")
        print("1. Cash")
        print("2. Card")
        
        choice = input("Choose a payment method (1-2): ").strip()
        if choice == "1":
            return "Cash"
        elif choice == "2":
            return "Card"
        else:
            print("Invalid choice.")
            return self.display_payment_methods()
