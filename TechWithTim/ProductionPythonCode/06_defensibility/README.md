# Defensibility

## Principle
**Defensibility**: Write code that fails safely and catches errors early.

Key concepts:
- **Fail-fast**: Detect and report errors immediately
- **Least privilege**: Give minimum necessary permissions
- **Safe defaults**: Choose secure, conservative defaults

## Bad Example (bad_payment.py)
- Silent failures
- Unsafe defaults
- No validation
- Errors discovered late
- Excessive permissions

## Good Example (good_payment.py)
- Validates input early
- Fails fast with clear errors
- Safe defaults
- Proper error handling
- Minimal permissions

## Quick Demo
```bash
python bad_payment.py
python good_payment.py
```

