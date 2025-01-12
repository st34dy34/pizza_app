from models.payment import PaymentProcessor, CashPayment, CardPayment
from views.payment_menu import PaymentMenu
from models.order import Order
from models.sales import Sales

class PaymentController:
    def __init__(self):
        self.payment_menu = PaymentMenu()
        self.sales = Sales()

    def handle_payment(self, order: Order):
        if order is None:
            print("No order to process. Please create an order first!")
            return

        if order.payment_status:
            print("The order has already been paid!")
            return

        if not order.pizzas:
            print("Cannot process payment for empty order!")
            return

        print(f"\n--- Payment ---")
        print(f"Total amount to pay: ${order.get_total():.2f}")
        method = self.payment_menu.display_payment_methods()

        if method == "Cash":
            payment_strategy = CashPayment()
        elif method == "Card":
            payment_strategy = CardPayment()
        else:
            print("Invalid payment method. Returning to the main menu.")
            return

        payment_processor = PaymentProcessor(payment_strategy, order)
        success = payment_processor.process_payment()

        if success:
            order.set_payment_status(True)
            self.sales.record_order(order)
            print("Payment successful!")
            print("Order recorded in sales system.")
            return True  # Return True to indicate successful payment
        else:
            print("Payment failed. Please try again.")
            return False