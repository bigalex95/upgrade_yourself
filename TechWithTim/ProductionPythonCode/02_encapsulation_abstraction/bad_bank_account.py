"""
BAD: No encapsulation - everything is exposed
"""


class BankAccount:
    """Everything is public - no protection!"""
    
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance  # Direct access allowed!
        self.transactions = []  # Can be manipulated directly!


if __name__ == "__main__":
    account = BankAccount("Alice", 1000)
    
    print(f"Initial balance: ${account.balance}")
    
    # Problem 1: Can directly modify balance without validation
    account.balance = -500  # Negative balance?!
    print(f"[X] After direct manipulation: ${account.balance}")
    
    # Problem 2: Can bypass business logic
    account.balance += 1000000  # Instant millionaire!
    print(f"[X] Became a millionaire: ${account.balance}")
    
    # Problem 3: Can corrupt internal state
    account.transactions = "not a list anymore"
    print(f"[X] Corrupted transactions: {account.transactions}")
    
    # Problem 4: If we change internal representation, all code breaks
    # e.g., if we want to store balance in cents instead of dollars
    
    print("\n[X] PROBLEMS:")
    print("- No validation or business rules enforced")
    print("- Internal state can be corrupted")
    print("- Can't change implementation without breaking clients")
    print("- No audit trail or control")

