"""
GOOD: Maintainable and testable calculator
"""
from typing import Optional, Tuple, Callable
from dataclasses import dataclass
from datetime import datetime


@dataclass
class CalculationResult:
    """Clear data structure for results"""
    expression: str
    result: float
    timestamp: datetime


class OperationParser:
    """Single responsibility: Parse expressions"""
    
    OPERATORS = ['+', '-', '*', '/']
    
    @staticmethod
    def parse(expr: str) -> Tuple[float, str, float]:
        """Parse expression into (operand1, operator, operand2)"""
        expr = expr.strip()
        
        for op in OperationParser.OPERATORS:
            if op in expr:
                parts = expr.split(op)
                if len(parts) != 2:
                    raise ValueError(f"Invalid expression: {expr}")
                
                try:
                    a = float(parts[0].strip())
                    b = float(parts[1].strip())
                    return a, op, b
                except ValueError:
                    raise ValueError(f"Invalid numbers in expression: {expr}")
        
        raise ValueError(f"No valid operator found in: {expr}")


class Operations:
    """Single responsibility: Mathematical operations (pure functions)"""
    
    @staticmethod
    def add(a: float, b: float) -> float:
        """Pure function - easy to test!"""
        return a + b
    
    @staticmethod
    def subtract(a: float, b: float) -> float:
        """Pure function - easy to test!"""
        return a - b
    
    @staticmethod
    def multiply(a: float, b: float) -> float:
        """Pure function - easy to test!"""
        return a * b
    
    @staticmethod
    def divide(a: float, b: float) -> float:
        """Pure function - easy to test!"""
        if b == 0:
            raise ValueError("Division by zero")
        return a / b
    
    @staticmethod
    def get_operation(operator: str) -> Callable[[float, float], float]:
        """Get operation function by operator symbol"""
        operations = {
            '+': Operations.add,
            '-': Operations.subtract,
            '*': Operations.multiply,
            '/': Operations.divide,
        }
        
        if operator not in operations:
            raise ValueError(f"Unknown operator: {operator}")
        
        return operations[operator]


class Calculator:
    """Clean calculator - delegates to specialized components"""
    
    def calculate(self, expr: str) -> float:
        """Calculate expression - simple and testable"""
        # Parse
        a, operator, b = OperationParser.parse(expr)
        
        # Get operation
        operation = Operations.get_operation(operator)
        
        # Calculate (pure function - no side effects!)
        result = operation(a, b)
        
        return result


class CalculatorWithHistory:
    """Calculator with history tracking - testable with dependency injection"""
    
    def __init__(self, calculator: Optional[Calculator] = None):
        self.calculator = calculator or Calculator()
        self.history = []
    
    def calculate(self, expr: str) -> CalculationResult:
        """Calculate and record in history"""
        result = self.calculator.calculate(expr)
        
        calc_result = CalculationResult(
            expression=expr,
            result=result,
            timestamp=datetime.now()
        )
        
        self.history.append(calc_result)
        return calc_result
    
    def get_history(self) -> list:
        """Get calculation history"""
        return self.history.copy()


if __name__ == "__main__":
    calc = CalculatorWithHistory()
    
    print("Basic Calculator:")
    print(f"5 + 3 = {calc.calculate('5 + 3').result}")
    print(f"10 - 4 = {calc.calculate('10 - 4').result}")
    print(f"6 * 7 = {calc.calculate('6 * 7').result}")
    print(f"20 / 5 = {calc.calculate('20 / 5').result}")
    
    print("\nHistory:")
    for entry in calc.get_history():
        print(f"  {entry.expression} = {entry.result}")
    
    print("\n[OK] BENEFITS:")
    print("- Each component has a single, clear responsibility")
    print("- Pure functions are easy to test")
    print("- No side effects in calculation logic")
    print("- Can test each component in isolation")
    print("- Easy to add new operations")
    print("- Clear, maintainable code structure")

