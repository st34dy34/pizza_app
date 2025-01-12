from controllers.order_controller import OrderController
from controllers.payment_controller import PaymentController
from controllers.admin_controller import AdminController

class MainController:
    def __init__(self):
        self.order_controller = OrderController()
        self.payment_controller = PaymentController()
        self.admin_controller = AdminController()

    def run(self):
        while True:
            print("\n--- Main Menu ---")
            print("1. Create Order")
            print("2. Process Payment")
            print("3. Admin Menu")
            print("4. Exit")

            choice = input("Choose an option (1-4): ").strip()

            if choice == "1":
                self.order_controller.handle_order()
            elif choice == "2":
                # Pass the actual order to handle_payment
                self.payment_controller.handle_payment(self.order_controller.current_order)
            elif choice == "3":
                self.admin_controller.handle_admin_tasks()
            elif choice == "4":
                print("Exiting application. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
