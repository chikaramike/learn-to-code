"""Assertions derived from the user story in odd_int.py."""

import pytest
from odd_int import find_it


@pytest.mark.parametrize(
    "seq, expected",
    [
        ([7], 7),
        ([0], 0),
        ([1, 1, 2], 2),
        ([0, 1, 0, 1, 0], 0),
        ([1, 2, 2, 3, 3, 3, 4, 3, 3, 3, 2, 2, 1], 4),
    ],
)
def test_find_it(seq, expected):
    assert find_it(seq) == expected
