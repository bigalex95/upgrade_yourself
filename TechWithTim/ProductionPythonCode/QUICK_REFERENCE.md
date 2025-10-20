# Quick Reference Guide

## Design Principles Cheat Sheet

### 1. Cohesion & SRP (Single Responsibility Principle)
**One class, one job**
- Each class should have only one reason to change
- High cohesion = related functionality grouped together
- Example: Separate UserRepository, EmailService, Validator classes

**Ask yourself:** "Can I describe this class's purpose in one sentence without using 'and'?"

---

### 2. Encapsulation & Abstraction
**Hide the details, show the interface**
- Keep internal state private
- Expose behavior, not data
- Use properties/getters for controlled access
- Abstract away complexity

**Ask yourself:** "If I change this internal implementation, will client code break?"

---

### 3. Loose Coupling & Modularity
**Depend on abstractions, not concrete implementations**
- Use interfaces/abstract base classes
- Inject dependencies (don't instantiate internally)
- Components should be swappable
- Minimize inter-module dependencies

**Ask yourself:** "Can I test this component without instantiating half my system?"

---

### 4. Reusability & Extensibility
**Open for extension, closed for modification**
- Use composition over inheritance
- Strategy pattern for variation
- Plugin architectures
- Don't hardcode behavior

**Ask yourself:** "Can I add new functionality without editing existing code?"

---

### 5. Portability
**Write once, run anywhere**
- Use cross-platform libraries (pathlib, not os.path)
- Environment variables for configuration
- Avoid platform-specific assumptions
- Abstract environment dependencies

**Ask yourself:** "Will this work on Linux, Windows, and Mac?"

---

### 6. Defensibility
**Fail fast, fail safe, fail loud**

**Fail-fast**: Validate input immediately
```python
if amount <= 0:
    raise ValueError("Amount must be positive")
```

**Least privilege**: Store/log only what's necessary
```python
# Store: "****-****-****-1234" 
# NOT: Full credit card number
```

**Safe defaults**: Conservative, secure defaults
```python
debug_mode=False  # Not True!
timeout=30  # Not None!
```

**Ask yourself:** "What's the worst that could happen with bad input?"

---

### 7. Maintainability & Testability
**Future you will thank present you**
- Write clear, self-documenting code
- Pure functions when possible
- Separate business logic from I/O
- Write tests!

**Pure function example:**
```python
def add(a, b):  # Pure: same input = same output
    return a + b

def add_and_log(a, b):  # Impure: side effects
    result = a + b
    print(f"Result: {result}")  # Side effect!
    return result
```

**Ask yourself:** "Can I write a unit test for this without mocking 5 things?"

---

### 8. Simplicity (KISS, DRY, YAGNI)

**KISS - Keep It Simple, Stupid**
- Prefer simple solutions over clever ones
- Avoid unnecessary abstractions
- If it's hard to explain, it's too complex

**DRY - Don't Repeat Yourself**
- Extract common logic into functions
- Single source of truth
- Repetition = maintenance burden

**YAGNI - You Aren't Gonna Need It**
- Don't build for hypothetical future needs
- Add features when actually needed
- Resist over-engineering

**Ask yourself:** 
- "Am I making this more complex than it needs to be?"
- "Have I written this exact logic elsewhere?"
- "Will I really need this feature?"

---

## Common Code Smells vs Solutions

| Code Smell | Principle Violated | Solution |
|------------|-------------------|----------|
| God class doing everything | SRP | Split into focused classes |
| Public fields everywhere | Encapsulation | Use private fields + methods |
| Hard-coded dependencies | Loose Coupling | Dependency injection |
| Giant if/else for types | Extensibility | Strategy/polymorphism |
| Hard-coded paths | Portability | Config files + pathlib |
| Silent failures | Defensibility | Fail-fast with exceptions |
| 500-line function | Maintainability | Break into smaller functions |
| Copy-pasted code | DRY | Extract to function |
| Unused "future" code | YAGNI | Delete it! |

---

## Quick Decision Tree

```
Is my class doing more than one thing?
├─ Yes → Split it (SRP)
└─ No → ✓

Can clients modify my internal state?
├─ Yes → Make it private (Encapsulation)
└─ No → ✓

Am I creating dependencies inside my class?
├─ Yes → Inject them (Loose Coupling)
└─ No → ✓

Do I need to edit existing code to add features?
├─ Yes → Use strategy/plugin pattern (Extensibility)
└─ No → ✓

Do I have hard-coded paths or platform assumptions?
├─ Yes → Use pathlib and config (Portability)
└─ No → ✓

Am I accepting input without validation?
├─ Yes → Validate and fail-fast (Defensibility)
└─ No → ✓

Would this be hard to test?
├─ Yes → Separate logic from I/O (Testability)
└─ No → ✓

Am I adding abstractions "just in case"?
├─ Yes → Remove it (YAGNI/KISS)
└─ No → ✓

Am I repeating this logic?
├─ Yes → Extract it (DRY)
└─ No → ✓
```

---

## Python-Specific Tips

### Use Built-in Features
```python
# ✅ Good: Use pathlib
from pathlib import Path
path = Path("data") / "file.txt"

# ❌ Bad: String concatenation
path = "data" + "/" + "file.txt"
```

### Type Hints for Clarity
```python
# ✅ Good: Clear interface
def process(data: List[str]) -> Dict[str, int]:
    ...

# ❌ Bad: Mystery function
def process(data):
    ...
```

### Use ABC for Interfaces
```python
from abc import ABC, abstractmethod

class Notifier(ABC):
    @abstractmethod
    def send(self, message: str):
        pass
```

### Dataclasses for Data
```python
from dataclasses import dataclass

@dataclass
class User:
    name: str
    email: str
    age: int
```

### Context Managers for Resources
```python
# ✅ Good: Automatic cleanup
with open('file.txt') as f:
    data = f.read()

# ❌ Bad: Manual cleanup
f = open('file.txt')
data = f.read()
f.close()  # Might be skipped on error!
```

---

## Remember

> "Any fool can write code that a computer can understand. 
> Good programmers write code that humans can understand."
> — Martin Fowler

> "Simplicity is prerequisite for reliability."
> — Edsger W. Dijkstra

> "Make it work, make it right, make it fast."
> — Kent Beck

---

**Keep this guide handy while coding! 📚✨**

