# Loose Coupling & Modularity

## Principle
**Coupling**: The degree of interdependence between modules
**Modularity**: Dividing a system into separate, interchangeable components

**Loose coupling** means components depend on abstractions, not concrete implementations.

## Bad Example (bad_notification.py)
- Tight coupling between OrderProcessor and EmailSender
- Hard-coded dependencies
- Difficult to test or swap implementations
- Changes ripple through the system

## Good Example (good_notification/)
- Components depend on interfaces (abstractions)
- Dependencies injected from outside
- Easy to test with mocks
- Can swap implementations without changing code
- Modular structure with clear boundaries

## Quick Demo
```bash
python bad_notification.py
python good_notification/main.py
```

