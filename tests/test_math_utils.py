"""Tests for math_utils module"""

import pytest
from math_utils import add, multiply, divide, is_even


class TestBasicOperations:
    """Test basic math operations."""
    
    def test_add_positive(self):
        """Test addition with positive numbers."""
        assert add(2, 3) == 5
        assert add(10, 15) == 25
   
    def test_add_negative(self):
        """Test addition with negative numbers."""
        assert add(-2, -3) == -5
        assert add(-10, 5) == -5
    
    def test_multiply_basic(self):
        """Test multiplication."""
        assert multiply(3, 4) == 12
        assert multiply(-2, 5) == -10
        assert multiply(0, 100) == 0
    
    def test_divide_basic(self):
        """Test division."""
        assert divide(10, 2) == 5
        assert divide(15, 3) == 5
        assert divide(-10, 2) == -5


class TestErrorHandling:
    """Test error conditions."""
    
    def test_add_type_error(self):
        """Test add with invalid types."""
        with pytest.raises(TypeError):
            add("2", 3)
        with pytest.raises(TypeError):
            add(2, None)
    
    def test_divide_by_zero(self):
        """Test division by zero."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(10, 0)
    
    def test_is_even_type_error(self):
        """Test is_even with invalid type."""
        with pytest.raises(TypeError):
            is_even(3.5)


class TestEvenNumbers:
    """Test even number checking."""
    
    def test_is_even_true(self):
        """Test even numbers."""
        assert is_even(2) is True
        assert is_even(0) is True
        assert is_even(100) is True
    
    def test_is_even_false(self):
        """Test odd numbers."""
        assert is_even(1) is False
        assert is_even(3) is False
        assert is_even(99) is False


# Parametrized tests
@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
    (10, -5, 5)
])
def test_add_multiple_inputs(a, b, expected):
    """Test add with multiple parameter sets."""
    assert add(a, b) == expected


@pytest.mark.parametrize("number,expected", [
    (0, True),
    (2, True),
    (1, False),
    (3, False)
])
def test_is_even_multiple_inputs(number, expected):
    """Test is_even with multiple inputs."""
    assert is_even(number) == expected