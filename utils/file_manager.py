import json
from pathlib import Path

class FileManager:
    def __init__(self, base_path: str = "data/orders"):
        self.base_path = Path(base_path)
        self.base_path.mkdir(parents=True, exist_ok=True)

    def save_order(self, order, order_id: str):
        order_data = {
            "pizzas": [
                {
                    "description": pizza.get_description(),
                    "cost": pizza.get_cost()
                }
                for pizza in order.pizzas
            ],
            "total_price": order.total_price,
            "payment_status": order.payment_status,
            "status": order.status
        }
        
        file_path = self.base_path / f"order_{order_id}.json"
        with open(file_path, "w") as f:
            json.dump(order_data, f, indent=4)

    def load_order(self, order_id: str) -> dict:
        file_path = self.base_path / f"order_{order_id}.json"
        try:
            with open(file_path, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            raise ValueError(f"Order {order_id} not found")