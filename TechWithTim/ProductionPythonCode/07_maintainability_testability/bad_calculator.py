"""
BAD: Hard to maintain and test
"""
import datetime


class Calculator:
    """Unmaintainable calculator with mixed concerns"""
    
    def __init__(self):
        self.history = []
        self.log_file = "calculator.log"
    
    def calculate(self, expr: str):
        """Complex method that does too many things"""
        
        # Logging mixed with business logic
        timestamp = datetime.datetime.now()
        
        # Complex parsing logic - hard to test separately
        if "+" in expr:
            parts = expr.split("+")
            if len(parts) != 2:
                # Writing to file - side effect!
                with open(self.log_file, "a") as f:
                    f.write(f"{timestamp}: ERROR - Invalid expression: {expr}\n")
                print(f"ERROR: Invalid expression")
                return None
            
            try:
                a = float(parts[0].strip())
                b = float(parts[1].strip())
            except:
                with open(self.log_file, "a") as f:
                    f.write(f"{timestamp}: ERROR - Invalid numbers in: {expr}\n")
                return None
            
            result = a + b
            
        elif "-" in expr:
            parts = expr.split("-")
            if len(parts) != 2:
                with open(self.log_file, "a") as f:
                    f.write(f"{timestamp}: ERROR - Invalid expression: {expr}\n")
                return None
            try:
                a = float(parts[0].strip())
                b = float(parts[1].strip())
            except:
                with open(self.log_file, "a") as f:
                    f.write(f"{timestamp}: ERROR - Invalid numbers in: {expr}\n")
                return None
            result = a - b
        
        elif "*" in expr:
            # More duplicated code...
            parts = expr.split("*")
            if len(parts) != 2:
                with open(self.log_file, "a") as f:
                    f.write(f"{timestamp}: ERROR - Invalid expression: {expr}\n")
                return None
            try:
                a = float(parts[0].strip())
                b = float(parts[1].strip())
            except:
                with open(self.log_file, "a") as f:
                    f.write(f"{timestamp}: ERROR - Invalid numbers in: {expr}\n")
                return None
            result = a * b
        
        else:
            with open(self.log_file, "a") as f:
                f.write(f"{timestamp}: ERROR - Unknown operator in: {expr}\n")
            return None
        
        # More side effects
        self.history.append((expr, result))
        with open(self.log_file, "a") as f:
            f.write(f"{timestamp}: {expr} = {result}\n")
        
        return result


if __name__ == "__main__":
    calc = Calculator()
    
    print(calc.calculate("5 + 3"))
    print(calc.calculate("10 - 4"))
    print(calc.calculate("6 * 7"))
    
    print("\n[X] PROBLEMS:")
    print("- Cannot test calculation logic without file I/O")
    print("- Lots of duplicated code")
    print("- Complex nested if/elif logic")
    print("- Side effects (file writing) mixed with computation")
    print("- Hard to add new operators")
    print("- Cannot mock time or file system for testing")
    print("- Difficult to understand and modify")

