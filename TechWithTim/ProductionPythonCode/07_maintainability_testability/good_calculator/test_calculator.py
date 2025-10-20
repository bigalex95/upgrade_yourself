"""
Comprehensive tests - demonstrating testability
"""
import unittest
from calculator import (
    Operations, 
    OperationParser, 
    Calculator, 
    CalculatorWithHistory
)


class TestOperations(unittest.TestCase):
    """Test pure mathematical operations"""
    
    def test_add(self):
        self.assertEqual(Operations.add(5, 3), 8)
        self.assertEqual(Operations.add(-5, 3), -2)
        self.assertEqual(Operations.add(0, 0), 0)
    
    def test_subtract(self):
        self.assertEqual(Operations.subtract(10, 4), 6)
        self.assertEqual(Operations.subtract(4, 10), -6)
    
    def test_multiply(self):
        self.assertEqual(Operations.multiply(6, 7), 42)
        self.assertEqual(Operations.multiply(5, 0), 0)
    
    def test_divide(self):
        self.assertEqual(Operations.divide(20, 5), 4)
        self.assertAlmostEqual(Operations.divide(10, 3), 3.333, places=2)
    
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            Operations.divide(10, 0)


class TestOperationParser(unittest.TestCase):
    """Test expression parsing"""
    
    def test_parse_addition(self):
        a, op, b = OperationParser.parse("5 + 3")
        self.assertEqual(a, 5)
        self.assertEqual(op, '+')
        self.assertEqual(b, 3)
    
    def test_parse_subtraction(self):
        a, op, b = OperationParser.parse("10 - 4")
        self.assertEqual(a, 10)
        self.assertEqual(op, '-')
        self.assertEqual(b, 4)
    
    def test_parse_with_whitespace(self):
        a, op, b = OperationParser.parse("  15  *  3  ")
        self.assertEqual(a, 15)
        self.assertEqual(op, '*')
        self.assertEqual(b, 3)
    
    def test_invalid_expression(self):
        with self.assertRaises(ValueError):
            OperationParser.parse("5 + 3 + 2")  # Too many operators
    
    def test_invalid_numbers(self):
        with self.assertRaises(ValueError):
            OperationParser.parse("abc + def")


class TestCalculator(unittest.TestCase):
    """Test calculator integration"""
    
    def setUp(self):
        self.calc = Calculator()
    
    def test_addition(self):
        result = self.calc.calculate("5 + 3")
        self.assertEqual(result, 8)
    
    def test_subtraction(self):
        result = self.calc.calculate("10 - 4")
        self.assertEqual(result, 6)
    
    def test_multiplication(self):
        result = self.calc.calculate("6 * 7")
        self.assertEqual(result, 42)
    
    def test_division(self):
        result = self.calc.calculate("20 / 5")
        self.assertEqual(result, 4)


class TestCalculatorWithHistory(unittest.TestCase):
    """Test calculator with history"""
    
    def setUp(self):
        self.calc = CalculatorWithHistory()
    
    def test_history_tracking(self):
        self.calc.calculate("5 + 3")
        self.calc.calculate("10 - 4")
        
        history = self.calc.get_history()
        self.assertEqual(len(history), 2)
        self.assertEqual(history[0].result, 8)
        self.assertEqual(history[1].result, 6)
    
    def test_history_returns_copy(self):
        """Test that get_history returns a copy, not the original"""
        self.calc.calculate("5 + 3")
        history1 = self.calc.get_history()
        history2 = self.calc.get_history()
        
        # Should be equal but not the same object
        self.assertEqual(len(history1), len(history2))
        self.assertIsNot(history1, history2)


def run_tests():
    """Run all tests"""
    unittest.main(argv=[''], verbosity=2, exit=False)


if __name__ == "__main__":
    print("Running comprehensive test suite...\n")
    run_tests()
    
    print("\n[OK] TESTABILITY BENEFITS:")
    print("- Pure functions are trivial to test")
    print("- Each component tested in isolation")
    print("- No mocking needed for core logic")
    print("- Tests are fast (no I/O)")
    print("- Easy to add new test cases")
    print("- Clear test structure")

