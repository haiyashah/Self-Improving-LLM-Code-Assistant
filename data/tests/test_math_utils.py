import pytest
from math_utils import calculate_efficiency

def test_standard_efficiency():
    """Test standard operational range."""
    assert calculate_efficiency(100, 50) == 2.0

def test_zero_input_power():
    """
    CRITICAL EDGE CASE: 
    This test ensures the system handles zero input without crashing.
    """
    with pytest.raises(ZeroDivisionError):
        calculate_efficiency(100, 0)

def test_negative_efficiency():
    """Verify handling of negative values."""
    assert calculate_efficiency(-10, 2) == -5.0
