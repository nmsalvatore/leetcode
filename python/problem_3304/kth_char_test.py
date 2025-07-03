from kth_char import Solution

def test_example1():
    solution = Solution()
    got = solution.kthCharacter(5)
    want = "b"
    assert got == want

def test_example2():
    solution = Solution()
    got = solution.kthCharacter(10)
    want = "c"
    assert got == want
