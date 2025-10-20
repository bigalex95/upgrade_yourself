"""
SMS implementation of Notifier interface
"""
from notifier import Notifier


class SMSNotifier(Notifier):
    """Concrete implementation for SMS"""
    
    def send(self, recipient: str, subject: str, message: str):
        print(f"[SMS] SMS to {recipient}")
        print(f"   {message}")

