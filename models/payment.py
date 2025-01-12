from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float) -> bool:
        pass

class CashPayment(PaymentStrategy):
    def pay(self, amount: float) -> bool:
        print(f"Processing cash payment of ${amount:.2f}")
        confirmation = input("Confirm payment? (y/n): ").strip().lower()
        return confirmation == "y"

class CardPayment(PaymentStrategy):
    def pay(self, amount: float) -> bool:
        print(f"Processing card payment of ${amount:.2f}")
        card_number = input("Enter card number: ").strip()
        expiration_date = input("Enter expiration date (MM/YY): ").strip()
        cvv = input("Enter CVV: ").strip()

        if len(card_number) == 16 and len(cvv) == 3:
            print("Payment approved!")
            return True
        else:
            print("Invalid card details. Payment failed.")
            return False

class PaymentProcessor:
    def __init__(self, strategy: PaymentStrategy, order):
        self.strategy = strategy
        self.order = order

    def process_payment(self) -> bool:
        return self.strategy.pay(self.order.get_total())  # Updated to use get_total()