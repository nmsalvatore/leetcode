#!/usr/bin/python3


class Solution:
    def add_binary(self, a: str, b: str) -> str:
        return format(int(a, base=2) + int(b, base=2), "b")
