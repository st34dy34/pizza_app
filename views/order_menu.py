class OrderMenu:
    @staticmethod
    def display_menu():
        print("\n1. Peperoni Pizza")
        print("2. Chilli Pizza")
        print("3. Zpět")
        
        choice = input("Vyberte možnosť (1-3): ").strip()
        if choice == "1":
            print("1")
        elif choice == "2":
            print("2")
        elif choice == "3":
            return
        else:
            print("Neplatná možnost.")
            OrderMenu.display_menu()
