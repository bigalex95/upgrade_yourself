"""
Order processor with dependency injection - loosely coupled
"""
from notifier import Notifier


class OrderProcessor:
    """Loosely coupled - depends on Notifier interface"""
    
    def __init__(self, notifier: Notifier):
        # Dependency injected - LOOSE COUPLING!
        self.notifier = notifier
    
    def process_order(self, order_id: int, customer_contact: str):
        print(f"Processing order {order_id}...")
        
        # Business logic
        print(f"  - Validating order...")
        print(f"  - Charging payment...")
        print(f"  - Updating inventory...")
        
        # Notification - uses injected notifier (any implementation!)
        self.notifier.send(
            customer_contact,
            f"Order {order_id} Confirmed",
            "Thank you for your order!"
        )
        
        print(f"Order {order_id} completed!\n")

