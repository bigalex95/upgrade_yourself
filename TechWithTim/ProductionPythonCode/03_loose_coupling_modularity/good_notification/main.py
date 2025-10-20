"""
GOOD: Loosely coupled system with dependency injection
"""
from order_processor import OrderProcessor
from email_notifier import EmailNotifier
from sms_notifier import SMSNotifier
from multi_notifier import MultiNotifier


if __name__ == "__main__":
    print("=== Scenario 1: Email notifications ===")
    email_notifier = EmailNotifier()
    processor = OrderProcessor(email_notifier)
    processor.process_order(12345, "customer@example.com")
    
    print("\n=== Scenario 2: SMS notifications ===")
    sms_notifier = SMSNotifier()
    processor = OrderProcessor(sms_notifier)
    processor.process_order(67890, "+1234567890")
    
    print("\n=== Scenario 3: Both email AND SMS ===")
    multi_notifier = MultiNotifier([email_notifier, sms_notifier])
    processor = OrderProcessor(multi_notifier)
    processor.process_order(11111, "customer@example.com / +1234567890")
    
    print("\n[OK] BENEFITS:")
    print("- OrderProcessor doesn't know or care HOW notification is sent")
    print("- Can easily swap email for SMS (or add more)")
    print("- Easy to test with a mock notifier")
    print("- Can compose multiple notifiers")
    print("- NO changes to OrderProcessor when adding new notification types")
    print("- Each module is independent and reusable")

