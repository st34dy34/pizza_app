from models.sales import Sales
from views.admin_menu import AdminMenu

class AdminController:
    def __init__(self):
        self.sales = Sales()
        self.admin_menu = AdminMenu()

    def handle_admin_tasks(self):
        if self.admin_menu.authenticate():
            self.display_sales_report()

    def display_sales_report(self):
        stats = self.sales.get_statistics()
        print("\n=== Sales Report ===")
        print(f"Total Sales: ${stats['Total Sales']:.2f}")
        print(f"Number of Orders: {stats['Number of Orders']}")
        print("\nRecent Orders:")
        for order in self.sales.orders[-5:]:  # Show last 5 orders
            print(f"\n{order}")