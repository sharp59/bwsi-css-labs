"""
tests_1d.py

This module contains unit tests for the two_sum function defined in lab_1d.py.
"""

import pytest
from labs.lab_1.lab_1d import two_sum


def test_basic():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]          # Classic example: nums[0] + nums[1] = 9
    assert two_sum([3, 2, 4], 6) == [1, 2]               # Answer is not at the start
    assert two_sum([3, 3], 6) == [0, 1]                  # Duplicate values, different indices


def test_negative_numbers():
    assert two_sum([-1, -2, -3, -4], -6) == [1, 3]       # Two negatives summing to negative target
    assert two_sum([-3, 4, 3, 90], 0) == [0, 2]          # Negative and positive summing to zero


def test_with_zeros():
    assert two_sum([0, 4, 3, 0], 0) == [0, 3]            # Two zeros summing to zero
    assert two_sum([0, 1, 2, 3], 3) == [0, 3]            # Zero paired with target itself


def test_large_target():
    assert two_sum([1, 2, 3, 1000000], 1000001) == [0, 3] # Large target value
    assert two_sum([500000, 500000], 1000000) == [0, 1]   # Two large equal numbers


def test_answer_not_at_start():
    assert two_sum([1, 2, 3, 4, 5], 9) == [3, 4]         # Answer near end of array
    assert two_sum([5, 3, 1, 2, 4], 3) == [2, 3]         # Answer in middle


if __name__ == "__main__":
    pytest.main()