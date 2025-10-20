"""
GOOD: Defensive programming - fail-fast, safe defaults, validation
"""
from dataclasses import dataclass
from decimal import Decimal
from typing import Optional
import re


class ValidationError(Exception):
    """Custom exception for validation errors"""
    pass


class PaymentError(Exception):
    """Custom exception for payment processing errors"""
    pass


@dataclass(frozen=True)
class PaymentResult:
    """Immutable payment result"""
    transaction_id: str
    amount: Decimal
    masked_account: str  # Only last 4 digits
    status: str


class PaymentValidator:
    """Separate validator - single responsibility"""
    
    @staticmethod
    def validate_amount(amount) -> Decimal:
        """Fail-fast: Validate amount immediately"""
        try:
            amount_decimal = Decimal(str(amount))
        except Exception:
            raise ValidationError(f"Invalid amount format: {amount}")
        
        if amount_decimal <= 0:
            raise ValidationError(f"Amount must be positive, got: {amount_decimal}")
        
        if amount_decimal > Decimal("10000"):
            raise ValidationError(f"Amount exceeds limit: {amount_decimal}")
        
        return amount_decimal
    
    @staticmethod
    def validate_account(account_number: str) -> str:
        """Fail-fast: Validate account number"""
        if not isinstance(account_number, str):
            raise ValidationError(f"Account number must be string, got: {type(account_number)}")
        
        # Remove dashes/spaces
        clean_account = account_number.replace("-", "").replace(" ", "")
        
        if not clean_account.isdigit():
            raise ValidationError("Account number must contain only digits")
        
        if len(clean_account) != 16:
            raise ValidationError(f"Account number must be 16 digits, got: {len(clean_account)}")
        
        return clean_account
    
    @staticmethod
    def validate_cvv(cvv: str) -> str:
        """Fail-fast: Validate CVV"""
        if not isinstance(cvv, str):
            raise ValidationError(f"CVV must be string, got: {type(cvv)}")
        
        if not cvv.isdigit():
            raise ValidationError("CVV must contain only digits")
        
        if len(cvv) not in [3, 4]:
            raise ValidationError(f"CVV must be 3 or 4 digits, got: {len(cvv)}")
        
        return cvv


class PaymentProcessor:
    """Defensive payment processor with safe defaults"""
    
    def __init__(self, 
                 debug_mode: bool = False,  # Safe default: OFF
                 max_retry: int = 3,  # Safe default: reasonable limit
                 timeout: int = 30):  # Safe default: 30 seconds
        
        self.debug_mode = debug_mode
        self.max_retry = max_retry
        self.timeout = timeout
        self._transaction_count = 0
    
    def process_payment(self, 
                       amount, 
                       account_number: str, 
                       cvv: str) -> PaymentResult:
        """Process payment with full validation and error handling"""
        
        # FAIL-FAST: Validate all inputs immediately
        validated_amount = PaymentValidator.validate_amount(amount)
        validated_account = PaymentValidator.validate_account(account_number)
        validated_cvv = PaymentValidator.validate_cvv(cvv)
        
        # LEAST PRIVILEGE: Only log necessary info, never sensitive data
        if self.debug_mode:
            masked = self._mask_account(validated_account)
            print(f"DEBUG: Processing ${validated_amount} from {masked}")
            # Note: CVV never logged!
        
        # Process payment
        try:
            result = self._charge_card(validated_amount, validated_account, validated_cvv)
        except Exception as e:
            # FAIL-FAST: Don't swallow exceptions
            raise PaymentError(f"Payment processing failed: {e}") from e
        
        # LEAST PRIVILEGE: Store minimal necessary data
        self._transaction_count += 1
        transaction_id = f"TXN-{self._transaction_count:06d}"
        
        # Create immutable result
        return PaymentResult(
            transaction_id=transaction_id,
            amount=validated_amount,
            masked_account=self._mask_account(validated_account),
            status="SUCCESS"
        )
    
    def _mask_account(self, account: str) -> str:
        """LEAST PRIVILEGE: Only show last 4 digits"""
        return f"****-****-****-{account[-4:]}"
    
    def _charge_card(self, amount: Decimal, account: str, cvv: str) -> bool:
        """Simulate charging with safeguards"""
        # In real code:
        # - Would have timeout (self.timeout)
        # - Would have retry limit (self.max_retry)
        # - Would use circuit breaker pattern
        # - Would never store CVV (PCI compliance)
        return True


if __name__ == "__main__":
    # SAFE DEFAULT: debug_mode is OFF by default
    processor = PaymentProcessor()
    
    print("Test 1: Valid payment")
    try:
        result = processor.process_payment(100.50, "1234-5678-9012-3456", "123")
        print(f"[OK] Success: {result}\n")
    except (ValidationError, PaymentError) as e:
        print(f"Error: {e}\n")
    
    print("Test 2: Negative amount - FAILS FAST")
    try:
        result = processor.process_payment(-500, "1234-5678-9012-3456", "123")
        print(f"Result: {result}\n")
    except ValidationError as e:
        print(f"[OK] Caught error immediately: {e}\n")
    
    print("Test 3: Invalid account number - FAILS FAST")
    try:
        result = processor.process_payment(100, "invalid", "123")
        print(f"Result: {result}\n")
    except ValidationError as e:
        print(f"[OK] Caught error immediately: {e}\n")
    
    print("Test 4: Missing CVV - FAILS FAST")
    try:
        # This will fail at the function signature level
        # In production, might use Optional[str] = None and validate
        result = processor.process_payment(100, "1234-5678-9012-3456", "")
        print(f"Result: {result}\n")
    except ValidationError as e:
        print(f"[OK] Caught error immediately: {e}\n")
    
    print("Test 5: Wrong data type - FAILS FAST")
    try:
        result = processor.process_payment("lots of money", 12345, [1, 2, 3])
        print(f"Result: {result}\n")
    except ValidationError as e:
        print(f"[OK] Caught error immediately: {e}\n")
    
    print("Test 6: Amount too large - FAILS FAST")
    try:
        result = processor.process_payment(1000000, "1234-5678-9012-3456", "123")
        print(f"Result: {result}\n")
    except ValidationError as e:
        print(f"[OK] Caught error immediately: {e}\n")
    
    print("\n[OK] BENEFITS:")
    print("- All inputs validated immediately (fail-fast)")
    print("- Clear error messages")
    print("- Safe defaults (debug OFF, reasonable limits, timeouts)")
    print("- Never stores sensitive data (CVV)")
    print("- Only logs/stores minimum necessary data (least privilege)")
    print("- Exceptions properly propagated (not swallowed)")
    print("- Immutable results prevent tampering")

