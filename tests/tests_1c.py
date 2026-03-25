"""
tests_1c.py

This module contains unit tests for the max_subarray_sum function defined in lab_1c.py.
"""

import pytest
from labs.lab_1.lab_1c import max_subarray_sum

def test_positive(): #all positives
    assert max_subarray_sum([1, 2, 3, 4]) == 10
    assert max_subarray_sum([1]) == 1
    assert max_subarray_sum([4, 3, 2]) == 9
    assert max_subarray_sum([0, 0, 0, 10]) == 10

def test_negative(): #all negatives
    assert max_subarray_sum([-1, -2, -3, -4]) == -1 
    assert max_subarray_sum([-2, -2, -1]) == -1

def test_mixed(): #mixed zeroes, positives, negatives
    assert max_subarray_sum([1, 0, 0, 1]) == 2
    assert max_subarray_sum([-2, 0, -2]) == 0
    assert max_subarray_sum([1, -1, -1, 1]) == 2
    assert max_subarray_sum([-10, 0, 1, 2, -5, 3, 4, -10]) == 7



if __name__ == "__main__":
    pytest.main()