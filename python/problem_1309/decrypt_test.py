from decrypt import Solution


def test_example_1():
    solution = Solution()
    got = solution.decryptString("10#11#12")
    want = "jkab"
    assert got == want


def test_example_2():
    solution = Solution()
    got = solution.decryptString("1326#")
    want = "acz"
    assert got == want
