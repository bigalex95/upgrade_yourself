"""
Email implementation of Notifier interface
"""
from notifier import Notifier


class EmailNotifier(Notifier):
    """Concrete implementation for email"""
    
    def send(self, recipient: str, subject: str, message: str):
        print(f"[EMAIL] EMAIL to {recipient}")
        print(f"   Subject: {subject}")
        print(f"   Message: {message}")

