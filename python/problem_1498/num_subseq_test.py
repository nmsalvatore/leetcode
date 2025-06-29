from num_subseq import Solution

def test_example1():
    solution = Solution()
    got = solution.num_subseq([3, 5, 6, 7], 9)
    want = 4
    assert got == want

def test_example2():
    solution = Solution()
    got = solution.num_subseq([3, 3, 6, 8], 10)
    want = 6
    assert got == want
