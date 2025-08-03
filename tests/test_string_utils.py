"""Tests for string_utils module"""

import pytest
from string_utils import reverse_string, count_words, is_palindrome


class TestStringOperations:
    """Test string manipulation functions."""
    
    def test_reverse_basic(self):
        """Test string reversal."""
        assert reverse_string("hello") == "olleh"
        assert reverse_string("") == ""
        assert reverse_string("a") == "a"
    
    def test_count_words_basic(self):
        """Test word counting."""
        assert count_words("hello world") == 2
        assert count_words("Python is awesome") == 3
        assert count_words("") == 0
        assert count_words("   ") == 0
    
    def test_palindrome_basic(self):
        """Test palindrome detection."""
        assert is_palindrome("racecar") is True
        assert is_palindrome("hello") is False
        assert is_palindrome("") is True
        assert is_palindrome("A") is True
    
    def test_palindrome_case_insensitive(self):
        """Test palindrome with mixed case."""
        assert is_palindrome("Racecar") is True
        assert is_palindrome("A man a plan a canal Panama") is True


class TestStringErrors:
    """Test string function error handling."""
    
    def test_reverse_type_error(self):
        """Test reverse with invalid type."""
        with pytest.raises(TypeError):
            reverse_string(123)
        with pytest.raises(TypeError):
            reverse_string(None)
    
    def test_count_words_type_error(self):
        """Test count_words with invalid type."""
        with pytest.raises(TypeError):
            count_words(123)
    
    def test_palindrome_type_error(self):
        """Test is_palindrome with invalid type."""
        with pytest.raises(TypeError):
            is_palindrome(123)


# Parametrized tests
@pytest.mark.parametrize("text,expected", [
    ("hello", "olleh"),
    ("Python", "nohtyP"),
    ("12345", "54321"),
    ("", "")
])
def test_reverse_multiple_inputs(text, expected):
    """Test reverse with multiple inputs."""
    assert reverse_string(text) == expected


@pytest.mark.parametrize("text,count", [
    ("hello world", 2),
    ("Python is great", 3),
    ("single", 1),
    ("", 0)
])
def test_count_words_multiple_inputs(text, count):
    """Test count_words with multiple inputs."""
    assert count_words(text) == count