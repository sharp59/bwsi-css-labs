"""
tests_1d.py

This module contains unit tests for the two_sum function defined in lab_1d.py.
"""

import pytest
from labs.lab_1.lab_1d import two_sum

def test_positive():
    assert two_sum([1, 2, 4, 4], 5) == [0, 2]
    assert two_sum([1, 2, 4, 4], 6) == [0, 3]
    assert two_sum([1, 2, 4, 4], 3) == [0, 1]

def test_negative():
    assert two_sum([-1, -2, -3, -4], -7) == [2, 3]
    assert two_sum([-1, 2], 1) == [0, 1]
    assert two_sum([1, 2, -10, 8], -8) == [1, 2]




if __name__ == "__main__":
    pytest.main()