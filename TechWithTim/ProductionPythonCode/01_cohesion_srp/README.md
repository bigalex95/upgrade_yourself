# Cohesion & Single Responsibility Principle (SRP)

## Principle
**SRP**: A class should have one, and only one, reason to change.
**Cohesion**: How closely related and focused the responsibilities of a module are.

## Bad Example (bad_user_manager.py)
- `UserManager` does everything: validation, database operations, email sending, reporting
- Low cohesion - unrelated responsibilities mixed together
- Hard to test, modify, or reuse individual pieces

## Good Example (good_user_manager.py)
- Each class has a single, well-defined responsibility
- High cohesion - related functions grouped together
- Easy to test, extend, and maintain each component independently

## Quick Demo
```bash
python bad_user_manager.py
python good_user_manager.py
```

