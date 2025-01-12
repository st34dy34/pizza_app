from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class CreateOrderCommand(Command):
    def __init__(self, order_controller):
        self.order_controller = order_controller

    def execute(self):
        self.order_controller.handle_order()

class ProcessPaymentCommand(Command):
    def __init__(self, payment_controller, order):
        self.payment_controller = payment_controller
        self.order = order

    def execute(self):
        self.payment_controller.handle_payment(self.order)