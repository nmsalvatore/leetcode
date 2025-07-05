from lucky_integer import Solution

def test_example1():
    solution = Solution()
    got = solution.findLucky([2, 2, 3, 4])
    want = 2
    assert got == want

def test_example2():
    solution = Solution()
    got = solution.findLucky([1, 2, 2, 3, 3, 3])
    want = 3
    assert got == want

def test_example3():
    solution = Solution()
    got = solution.findLucky([2, 2, 2, 3, 3])
    want = -1
    assert got == want
