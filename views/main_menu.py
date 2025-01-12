from views.ui import UI
from controllers.payment_controller import PaymentController
from controllers.admin_controller import AdminController
from controllers.order_controller import OrderController

class MainMenu(UI):
    def __init__(self):
        self.order_controller = OrderController()
        self.payment_controller = PaymentController()
        self.admin_controller = AdminController()
    
    def write_out(self):
        print("\n--- Main Menu ---")
        print("1. Create Order")
        print("2. Process Payment")
        print("3. Admin Menu")
        print("4. Exit Application")

    def handle_choice(self, choice):
        if choice == "1":
            self.order_controller.handle_order()
        elif choice == "2":
            if self.payment_controller.handle_payment(self.order_controller.current_order):
                # Create a new order after successful payment
                self.order_controller.current_order = None
        elif choice == "3":
            self.admin_controller.handle_admin_tasks()
        elif choice == "4":
            print("Thank you for using our Pizza Order Application!")
            exit()
        else:
            print("Invalid choice. Please try again.")