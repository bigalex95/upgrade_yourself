"""
BAD: Not defensive - silent failures, unsafe defaults, no validation
"""


class PaymentProcessor:
    """Unsafe payment processor - many security and reliability issues"""
    
    def __init__(self):
        self.transactions = []
        self.debug_mode = True  # Unsafe default!
        self.max_retry = 100  # Excessive default!
        self.timeout = None  # No timeout - can hang forever!
    
    def process_payment(self, amount, account_number, cvv=None):
        """Process payment - no validation, silent failures"""
        
        # No validation - accepts any input!
        # Negative amounts? Sure!
        # Strings instead of numbers? Sure!
        # Missing required fields? Sure!
        
        if self.debug_mode:
            # Logging sensitive data - SECURITY ISSUE!
            print(f"DEBUG: Processing ${amount} from {account_number}, CVV: {cvv}")
        
        # Simulate payment processing
        try:
            # No input validation
            result = self._charge_card(amount, account_number, cvv)
            
            # Silent failure - just returns None
            if not result:
                return None
            
            self.transactions.append({
                'amount': amount,
                'account': account_number,  # Storing full account number!
                'cvv': cvv  # Storing CVV - MAJOR SECURITY ISSUE!
            })
            
            return result
        
        except Exception as e:
            # Swallowing exceptions - silent failure!
            if self.debug_mode:
                print(f"Error occurred: {e}")
            return None
    
    def _charge_card(self, amount, account, cvv):
        """Simulate charging - no safeguards"""
        # In real code, would call payment API
        # No retry limits, no timeouts, no circuit breaker
        return True


if __name__ == "__main__":
    processor = PaymentProcessor()
    
    print("Test 1: Valid payment")
    result = processor.process_payment(100.50, "1234-5678-9012-3456", "123")
    print(f"Result: {result}\n")
    
    print("Test 2: Negative amount - should fail but doesn't!")
    result = processor.process_payment(-500, "1234-5678-9012-3456", "123")
    print(f"Result: {result} [X] Accepted negative amount!\n")
    
    print("Test 3: Invalid account number - no validation!")
    result = processor.process_payment(100, "invalid", "123")
    print(f"Result: {result} [X] Accepted invalid account!\n")
    
    print("Test 4: Missing CVV - no validation!")
    result = processor.process_payment(100, "1234-5678-9012-3456")
    print(f"Result: {result} [X] Accepted missing CVV!\n")
    
    print("Test 5: Wrong data type - no validation!")
    result = processor.process_payment("lots of money", 12345, [1, 2, 3])
    print(f"Result: {result} [X] Accepted wrong types!\n")
    
    print("[X] PROBLEMS:")
    print("- No input validation")
    print("- Silent failures (returns None instead of raising errors)")
    print("- Stores sensitive data (CVV) - PCI compliance violation!")
    print("- Debug mode ON by default - leaks sensitive info")
    print("- No timeout - can hang forever")
    print("- Excessive retry limit (100)")
    print("- Errors discovered late or never")

