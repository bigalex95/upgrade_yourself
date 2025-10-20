# Reusability & Extensibility

## Principle
**Reusability**: Code can be used in multiple contexts without modification
**Extensibility**: New functionality can be added without modifying existing code (Open/Closed Principle)

## Bad Example (bad_report.py)
- Hard-coded logic for specific use cases
- Must modify existing code to add new formats
- Difficult to reuse components separately
- Lots of if/else chains

## Good Example (good_report.py)
- Plugin architecture for easy extension
- Reusable components
- Add new formats without touching existing code
- Strategy pattern for flexibility

## Quick Demo
```bash
python bad_report.py
python good_report.py
```

