"""
Abstract interface for notifications - enables loose coupling
"""
from abc import ABC, abstractmethod


class Notifier(ABC):
    """Abstract base class - defines the interface"""
    
    @abstractmethod
    def send(self, recipient: str, subject: str, message: str):
        """Send a notification"""
        pass

