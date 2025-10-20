"""
Composite notifier - sends via multiple channels
"""
from typing import List
from notifier import Notifier


class MultiNotifier(Notifier):
    """Sends notifications through multiple channels"""
    
    def __init__(self, notifiers: List[Notifier]):
        self.notifiers = notifiers
    
    def send(self, recipient: str, subject: str, message: str):
        for notifier in self.notifiers:
            notifier.send(recipient, subject, message)

