from palindrome import Solution

def test_example1():
    solution = Solution()
    got = solution.isPalindrome(121)
    want = True
    assert got == want

def test_example2():
    solution = Solution()
    got = solution.isPalindrome(-121)
    want = False
    assert got == want

def test_example3():
    solution = Solution()
    got = solution.isPalindrome(10)
    want = False
    assert got == want
