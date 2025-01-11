class PaymentMenu:
    @staticmethod
    def display_menu():
        print("\nZobrazení objednávky:")
        # Add functionality to display the current order here
        print("Vyberte platební metodu:")
        print("1. Hotovost")
        print("2. Karta")
        print("3. Zpět")
        
        choice = input("Vyberte možnosť (1-3): ").strip()
        if choice == "1":
            print("Platba hotovostí.")
        elif choice == "2":
            print("Platba kartou.")
        elif choice == "3":
            return
        else:
            print("Neplatná možnost.")
            PaymentMenu.display_menu()
