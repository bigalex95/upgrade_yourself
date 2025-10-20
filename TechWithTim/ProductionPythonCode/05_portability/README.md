# Portability

## Principle
**Portability**: Code should work across different platforms, environments, and configurations without modification.

Key aspects:
- Use cross-platform libraries
- Avoid hard-coded paths
- Abstract environment-specific details
- Use configuration files

## Bad Example (bad_file_handler.py)
- Hard-coded Windows paths
- Platform-specific code
- Environment assumptions baked in
- Won't work on Linux/Mac

## Good Example (good_file_handler.py)
- Cross-platform path handling
- Environment abstraction
- Configuration-driven
- Works on any OS

## Quick Demo
```bash
python bad_file_handler.py
python good_file_handler.py
```

