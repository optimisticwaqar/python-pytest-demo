"""String Utilities for Testing Demo"""

def reverse_string(text):
    """Reverse a string."""
    if not isinstance(text, str):
        raise TypeError("Argument must be a string")
    return text[::-1]

def count_words(text):
    """Count words in a string."""
    if not isinstance(text, str):
        raise TypeError("Argument must be a string")
    return len(text.split()) if text.strip() else 0

def is_palindrome(text):
    """Check if string is palindrome (ignoring case)."""
    if not isinstance(text, str):
        raise TypeError("Argument must be a string")
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]