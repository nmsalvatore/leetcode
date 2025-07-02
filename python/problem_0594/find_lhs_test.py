from find_lhs import Solution

def test_example1():
    solution = Solution()
    got = solution.findLHS([1,3,2,2,5,2,3,7])
    want = 5
    assert got == want

def test_example2():
    solution = Solution()
    got = solution.findLHS([1,2,3,4])
    want = 2
    assert got == want
