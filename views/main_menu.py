from views.ui import UI
from views.order_menu import OrderMenu
from views.payment_menu import PaymentMenu
from views.admin_menu import AdminMenu

class Main_menu(UI):
    @staticmethod 
    def write_out():
            print("\nHlavní menu:")
            print("1. Vytvořit objednávku")
            print("2. Platba")
            print("3. Admin menu")
            print("4. Ukončit aplikaci")
    
    @staticmethod
    def handle_choice(choice):
        if choice == "1":
            OrderMenu.display_menu()
        elif choice == "2":
            PaymentMenu.display_menu()
        elif choice == "3":
            AdminMenu.display_menu()
        elif choice == "4":
            exit()
        else:
            print("Neplatná možnost!")