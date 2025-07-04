from add_two_nums import ListNode, Solution

def test_example1():
    solution = Solution()
    got = solution.addTwoNumbers(
        ListNode(2, ListNode(4, ListNode(3))),
        ListNode(5, ListNode(6, ListNode(4)))
    )
    want = ListNode(7, ListNode(0, ListNode(8)))
    assert got == want

def test_example2():
    solution = Solution()
    got = solution.addTwoNumbers(
        ListNode(0),
        ListNode(0)
    )
    want = ListNode(0)
    assert got == want

def test_example3():
    solution = Solution()
    got = solution.addTwoNumbers(
        ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))),
        ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
    )
    want = ListNode(8, ListNode(9, ListNode(9, ListNode(9, ListNode(0, ListNode(0, ListNode(0, ListNode(1))))))))
    assert got == want
