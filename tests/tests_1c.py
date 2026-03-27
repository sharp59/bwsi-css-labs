"""
tests_1c.py

This module contains unit tests for the max_subarray_sum function defined in lab_1c.py.
"""

import pytest
from labs.lab_1.lab_1c import max_subarray_sum


def test_mixed_numbers():
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6   # Classic LeetCode example: [4,-1,2,1]
    assert max_subarray_sum([-2, -3, 4, -1, -2, 1, 5, -3]) == 7      # Subarray: [4,-1,-2,1,5]


def test_all_positive():
    assert max_subarray_sum([1, 2, 3, 4, 5]) == 15                    # Entire array is optimal
    assert max_subarray_sum([5]) == 5                                  # Single positive element


def test_all_negative():
    assert max_subarray_sum([-3, -1, -2]) == -1                       # Least negative single element
    assert max_subarray_sum([-5]) == -5                               # Single negative element


def test_single_element():
    assert max_subarray_sum([0]) == 0                                  # Single zero
    assert max_subarray_sum([42]) == 42                               # Single large positive
    assert max_subarray_sum([-42]) == -42                             # Single large negative


def test_with_zeros():
    assert max_subarray_sum([0, 0, 0]) == 0                           # All zeros
    assert max_subarray_sum([-1, 0, -2]) == 0                         # Zero is the best option
    assert max_subarray_sum([0, 3, -1, 0]) == 3                       # Zero boundaries around subarray


def test_large_swings():
    assert max_subarray_sum([100, -200, 100]) == 100                  # Two equal isolated peaks
    assert max_subarray_sum([-1, -1, 10, -1, -1]) == 10              # Single dominant element


if __name__ == "__main__":
    pytest.main()