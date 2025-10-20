# Maintainability & Testability

## Principle
**Maintainability**: Code should be easy to understand, modify, and debug
**Testability**: Code should be easy to test in isolation

Key aspects:
- Clear structure and naming
- Pure functions when possible
- Dependency injection for testing
- Separation of concerns

## Bad Example (bad_calculator.py)
- Complex, nested logic
- Side effects mixed with computation
- Hard-coded dependencies
- Difficult to test
- No tests included

## Good Example (good_calculator/)
- Clear, simple functions
- Pure functions
- Easy to test
- Comprehensive test suite included
- Well-documented

## Quick Demo
```bash
python bad_calculator.py
python good_calculator/calculator.py
python good_calculator/test_calculator.py
```

