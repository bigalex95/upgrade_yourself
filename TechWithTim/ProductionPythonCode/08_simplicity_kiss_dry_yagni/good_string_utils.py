"""
GOOD: Simple, DRY, and only what's needed
Follows KISS, DRY, and YAGNI
"""


def change_case(text: str, case_type: str) -> str:
    """
    KISS: Simple function for case conversion
    No unnecessary classes or factories
    """
    case_type = case_type.lower()
    
    if case_type == 'upper':
        return text.upper()
    elif case_type == 'lower':
        return text.lower()
    elif case_type == 'title':
        return text.title()
    else:
        raise ValueError(f"Unknown case type: {case_type}")


def greet_user(name: str, time_of_day: str = "day") -> str:
    """
    DRY: Single function with parameter instead of 3 separate functions
    Logic written once, reused for all times of day
    """
    # Handle empty name
    if not name:
        name = "Guest"
    
    # Truncate long names
    if len(name) > 20:
        name = name[:20] + "..."
    
    return f"Hello, {name}! Good {time_of_day}!"


def reverse_string(text: str) -> str:
    """
    KISS: Use Python's simple string slicing
    No need for complex loops
    """
    return text[::-1]


def truncate_text(text: str, max_length: int, suffix: str = "...") -> str:
    """
    KISS: Simple, single-purpose function
    Only added because it's actually needed
    """
    if len(text) <= max_length:
        return text
    return text[:max_length] + suffix


# YAGNI: No unused "future features" here!
# Only implement what's actually needed right now.
# When translation is needed, add it then.


if __name__ == "__main__":
    print("=== Case Conversion (KISS) ===")
    text = "hello world"
    print(f"Original: {text}")
    print(f"Upper: {change_case(text, 'upper')}")
    print(f"Lower: {change_case(text.upper(), 'lower')}")
    print(f"Title: {change_case(text, 'title')}")
    
    print("\n=== Greetings (DRY) ===")
    print(greet_user("Alice", "morning"))
    print(greet_user("Bob", "afternoon"))
    print(greet_user("Charlie", "evening"))
    print(greet_user("", "morning"))  # Empty name
    print(greet_user("VeryLongNameThatExceedsTwentyCharacters", "day"))
    
    print("\n=== String Reversal (KISS) ===")
    print(f"Reverse 'hello': {reverse_string('hello')}")
    print(f"Reverse 'Python': {reverse_string('Python')}")
    
    print("\n=== Truncate (YAGNI) ===")
    long_text = "This is a very long text that needs truncation"
    print(truncate_text(long_text, 20))
    print(truncate_text(long_text, 30, "..."))
    
    print("\n[OK] BENEFITS:")
    print("- KISS: Simple, straightforward code")
    print("- DRY: No repeated logic")
    print("- YAGNI: Only what's needed, nothing extra")
    print("- Easy to understand and modify")
    print("- Less code to maintain and test")
    print("- Leverages Python's built-in features")
    
    print("\n[OK] COMPARISON:")
    print(f"Bad example: ~100+ lines with classes, factories, enums")
    print(f"Good example: ~70 lines with simple functions")
    print(f"Same functionality, much simpler!")

