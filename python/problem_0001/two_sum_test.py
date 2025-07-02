from two_sum import Solution

def test_example1():
    solution = Solution()
    got = solution.twoSum([2, 7, 11, 15], 9)
    want = [0, 1]
    assert got == want

def test_example2():
    solution = Solution()
    got = solution.twoSum([3, 2, 4], 6)
    want = [1, 2]
    assert got == want

def test_example3():
    solution = Solution()
    got = solution.twoSum([3, 3], 6)
    want = [0, 1]
    assert got == want

def test_case40():
    solution = Solution()
    got = solution.twoSum([-3, 4, 3, 90], 0)
    want = [0, 2]
    assert got == want
