"""
GOOD: Proper encapsulation and abstraction
"""
from typing import List
from datetime import datetime


class Transaction:
    """Encapsulates transaction details"""
    
    def __init__(self, amount: float, transaction_type: str, description: str):
        self._amount = amount
        self._type = transaction_type
        self._timestamp = datetime.now()
        self._description = description
    
    def __str__(self):
        return f"{self._timestamp.strftime('%Y-%m-%d %H:%M')} | {self._type:10} | ${self._amount:8.2f} | {self._description}"


class BankAccount:
    """Encapsulated bank account with controlled access"""
    
    def __init__(self, owner: str, initial_balance: float = 0):
        self._owner = owner
        self._balance = initial_balance  # Private attribute
        self._transactions: List[Transaction] = []  # Private attribute
        
        if initial_balance > 0:
            self._add_transaction(initial_balance, "DEPOSIT", "Initial deposit")
    
    # Public interface - abstraction of account operations
    
    def deposit(self, amount: float, description: str = "Deposit"):
        """Deposit money - with validation"""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        
        self._balance += amount
        self._add_transaction(amount, "DEPOSIT", description)
        return self._balance
    
    def withdraw(self, amount: float, description: str = "Withdrawal"):
        """Withdraw money - with validation"""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        
        self._balance -= amount
        self._add_transaction(-amount, "WITHDRAWAL", description)
        return self._balance
    
    def get_balance(self) -> float:
        """Read-only access to balance"""
        return self._balance
    
    def get_statement(self) -> List[str]:
        """Get transaction history - returns copy, not original"""
        return [str(t) for t in self._transactions]
    
    # Private helper methods - implementation details
    
    def _add_transaction(self, amount: float, trans_type: str, description: str):
        """Internal method to record transactions"""
        transaction = Transaction(amount, trans_type, description)
        self._transactions.append(transaction)
    
    def __str__(self):
        return f"Account({self._owner}): ${self._balance:.2f}"


if __name__ == "__main__":
    account = BankAccount("Alice", 1000)
    
    print(f"[OK] Initial: {account}")
    
    # Proper way: Use public interface
    account.deposit(500, "Salary")
    print(f"[OK] After deposit: {account}")
    
    account.withdraw(200, "Groceries")
    print(f"[OK] After withdrawal: {account}")
    
    # Try to do something invalid
    try:
        account.withdraw(10000, "Mansion")
    except ValueError as e:
        print(f"[OK] Validation works: {e}")
    
    try:
        account.deposit(-100, "Hacking attempt")
    except ValueError as e:
        print(f"[OK] Validation works: {e}")
    
    # Can't directly access private attributes (convention)
    # account._balance = -500  # Can do this, but Python convention says DON'T
    
    # Read balance safely
    print(f"\n[OK] Current balance: ${account.get_balance():.2f}")
    
    # Get statement (protected copy)
    print("\n[OK] Transaction History:")
    for statement_line in account.get_statement():
        print(f"   {statement_line}")
    
    print("\n[OK] BENEFITS:")
    print("- Business rules enforced (no negative balance)")
    print("- Internal state protected from corruption")
    print("- Can change internal implementation freely")
    print("- Clean, simple interface for clients")
    print("- Automatic audit trail")

