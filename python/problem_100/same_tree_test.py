#!/usr/bin/python3

from same_tree import Solution, TreeNode


def test_example_1():
    solution = Solution()

    p = TreeNode(1, TreeNode(2), TreeNode(3))
    q = TreeNode(1, TreeNode(2), TreeNode(3))

    got = solution.is_same_tree(p, q)
    want = True

    assert got == want


def test_example_2():
    solution = Solution()

    p = TreeNode(1, TreeNode(2))
    q = TreeNode(1, None, TreeNode(2))

    got = solution.is_same_tree(p, q)
    want = False

    assert got == want


def test_example_3():
    solution = Solution()

    p = TreeNode(1, TreeNode(2), TreeNode(1))
    q = TreeNode(1, TreeNode(1), TreeNode(2))

    got = solution.is_same_tree(p, q)
    want = False

    assert got == want
