#!/usr/bin/python3


class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_same_tree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return (self.is_same_tree(p.left, q.left) and
                self.is_same_tree(p.right, q.right))
