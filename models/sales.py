class Sales:
# --- /SINGLETON PATTERN/ ---
    _instance = None  # Class-level attribute to hold the single instance

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:  # Check if an instance already exists
            cls._instance = super().__new__(cls)
            # Initialize sales data
            cls._instance.total_sales = 0
            cls._instance.orders = []
        return cls._instance

# --- /SINGLETON PATTERN/ ---
    def record_order(self, order):
        """Record a new order and update total sales."""
        self.orders.append(order)
        self.total_sales += order.total_price

    def get_statistics(self):
        """Retrieve sales statistics."""
        return {
            "Total Sales": self.total_sales,
            "Number of Orders": len(self.orders)
        }

    def __str__(self):
        """String representation of sales statistics."""
        stats = self.get_statistics()
        return f"Total Sales: ${stats['Total Sales']}\nNumber of Orders: {stats['Number of Orders']}"
