#!/usr/bin/python3

from add_binary import Solution


def test_example_1():
    solution = Solution()
    got = solution.add_binary("11", "1")
    want = "100"
    assert got == want


def test_example_2():
    solution = Solution()
    got = solution.add_binary("1010", "1011")
    want = "10101"
    assert got == want
