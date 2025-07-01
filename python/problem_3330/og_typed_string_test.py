from og_typed_string import Solution

def test_example1():
    solution = Solution()
    got = solution.possibleStringCount("abbcccc")
    want = 5
    assert got == want

def test_example2():
    solution = Solution()
    got = solution.possibleStringCount("abcd")
    want = 1
    assert got == want

def test_example3():
    solution = Solution()
    got = solution.possibleStringCount("aaaa")
    want = 4
    assert got == want
