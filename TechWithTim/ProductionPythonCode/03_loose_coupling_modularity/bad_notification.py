"""
BAD: Tightly coupled - components directly depend on each other
"""


class EmailSender:
    """Concrete email implementation"""
    
    def send_email(self, to: str, subject: str, body: str):
        print(f"[EMAIL] Sending email to {to}: {subject}")


class OrderProcessor:
    """Tightly coupled to EmailSender"""
    
    def __init__(self):
        # Hard-coded dependency - TIGHT COUPLING!
        self.email_sender = EmailSender()
    
    def process_order(self, order_id: int, customer_email: str):
        print(f"Processing order {order_id}...")
        
        # Business logic
        print(f"  - Validating order...")
        print(f"  - Charging payment...")
        print(f"  - Updating inventory...")
        
        # Notification - directly calls EmailSender
        self.email_sender.send_email(
            customer_email,
            f"Order {order_id} Confirmed",
            "Thank you for your order!"
        )
        
        print(f"Order {order_id} completed!\n")


if __name__ == "__main__":
    processor = OrderProcessor()
    processor.process_order(12345, "customer@example.com")
    
    print("[X] PROBLEMS:")
    print("- OrderProcessor is tightly coupled to EmailSender")
    print("- Can't test OrderProcessor without sending emails")
    print("- Can't switch to SMS without modifying OrderProcessor")
    print("- Can't send both email AND SMS")
    print("- Hard to unit test in isolation")
    
    print("\n[X] What if we want SMS notifications?")
    print("   → Must modify OrderProcessor code")
    print("   → Must create if/else logic for notification type")
    print("   → Violates Open/Closed Principle")

