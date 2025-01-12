from abc import ABC, abstractmethod

class OrderObserver(ABC):
    @abstractmethod
    def update(self, order_status: str):
        pass

class OrderNotifier(OrderObserver):
    def update(self, order_status: str):
        print(f"Order Status Update: {order_status}")