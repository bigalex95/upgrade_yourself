"""
BAD: Over-engineered, repetitive, with unnecessary features
Violates KISS, DRY, and YAGNI
"""
from abc import ABC, abstractmethod
from enum import Enum
from typing import Optional


class StringCase(Enum):
    """YAGNI: Do we really need an enum for this?"""
    UPPER = "upper"
    LOWER = "lower"
    TITLE = "title"
    CAPITALIZE = "capitalize"


class StringTransformerInterface(ABC):
    """KISS violation: Unnecessary abstraction for simple string operations"""
    
    @abstractmethod
    def transform(self, text: str) -> str:
        pass


class UpperCaseTransformer(StringTransformerInterface):
    """KISS violation: Class for a one-line operation"""
    def transform(self, text: str) -> str:
        return text.upper()


class LowerCaseTransformer(StringTransformerInterface):
    """KISS violation: Another class for a one-line operation"""
    def transform(self, text: str) -> str:
        return text.lower()


class TitleCaseTransformer(StringTransformerInterface):
    """KISS violation: Yet another class"""
    def transform(self, text: str) -> str:
        return text.title()


class TransformerFactory:
    """KISS violation: Factory for simple string operations!"""
    
    @staticmethod
    def create_transformer(case_type: StringCase) -> StringTransformerInterface:
        if case_type == StringCase.UPPER:
            return UpperCaseTransformer()
        elif case_type == StringCase.LOWER:
            return LowerCaseTransformer()
        elif case_type == StringCase.TITLE:
            return TitleCaseTransformer()
        else:
            raise ValueError(f"Unknown case type: {case_type}")


class StringProcessor:
    """Repetitive code and over-engineered features"""
    
    def __init__(self):
        self.factory = TransformerFactory()
    
    # DRY violation: Repetitive greeting methods
    def greet_user_morning(self, name: str):
        """Repeated logic"""
        if not name:
            return "Hello, Guest! Good morning!"
        if len(name) > 20:
            name = name[:20] + "..."
        return f"Hello, {name}! Good morning!"
    
    def greet_user_afternoon(self, name: str):
        """Same logic, different greeting - DRY violation!"""
        if not name:
            return "Hello, Guest! Good afternoon!"
        if len(name) > 20:
            name = name[:20] + "..."
        return f"Hello, {name}! Good afternoon!"
    
    def greet_user_evening(self, name: str):
        """More repetition!"""
        if not name:
            return "Hello, Guest! Good evening!"
        if len(name) > 20:
            name = name[:20] + "..."
        return f"Hello, {name}! Good evening!"
    
    # YAGNI violation: Features that aren't needed yet
    def future_feature_translate(self, text: str, language: str):
        """YAGNI: Not needed now, may never be needed"""
        # Placeholder for future translation feature
        return text
    
    def future_feature_sentiment_analysis(self, text: str):
        """YAGNI: Building for hypothetical future"""
        # Placeholder for sentiment analysis
        return "neutral"
    
    def future_feature_text_to_speech(self, text: str):
        """YAGNI: Yet another unused feature"""
        pass
    
    # Over-complicated string reversal
    def reverse_string_complex(self, text: str) -> str:
        """KISS violation: Unnecessarily complex"""
        result = []
        index = len(text) - 1
        while index >= 0:
            char = text[index]
            result.append(char)
            index = index - 1
        return ''.join(result)


if __name__ == "__main__":
    processor = StringProcessor()
    
    # Using the over-engineered transformer
    transformer = processor.factory.create_transformer(StringCase.UPPER)
    print(transformer.transform("hello"))
    
    # Using repetitive greeting methods
    print(processor.greet_user_morning("Alice"))
    print(processor.greet_user_afternoon("Bob"))
    print(processor.greet_user_evening("Charlie"))
    
    # Complex string reversal
    print(processor.reverse_string_complex("hello"))
    
    print("\n[X] PROBLEMS:")
    print("- KISS: Over-engineered with unnecessary classes and factories")
    print("- DRY: Repeated greeting logic in 3 methods")
    print("- YAGNI: Unused 'future' features cluttering code")
    print("- Simple operations wrapped in complex abstractions")
    print("- Hard to understand and maintain")
    print("- More code to test and debug")

