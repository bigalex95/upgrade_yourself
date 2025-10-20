# Encapsulation & Abstraction

## Principle
**Encapsulation**: Hide internal implementation details, expose only what's necessary
**Abstraction**: Provide a simple interface that hides complexity

## Bad Example (bad_bank_account.py)
- Internal data directly accessible and modifiable
- Implementation details exposed
- No validation or protection
- Clients must know internal structure

## Good Example (good_bank_account.py)
- Private attributes with controlled access
- Implementation hidden behind clear interface
- Validation and business rules enforced
- Clients work with simple, abstract operations

## Quick Demo
```bash
python bad_bank_account.py
python good_bank_account.py
```

