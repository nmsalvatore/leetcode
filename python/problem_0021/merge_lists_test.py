from merge_lists import ListNode, Solution

def test_example1():
    solution = Solution()
    got = solution.mergeTwoLists(
        ListNode(1, ListNode(2, ListNode(4))),
        ListNode(1, ListNode(3, ListNode(4)))
    )
    want = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4))))))
    assert got == want

def test_example2():
    solution = Solution()
    got = solution.mergeTwoLists(None, None)
    want = None
    assert got == want

def test_example3():
    solution = Solution()
    got = solution.mergeTwoLists(None, ListNode())
    want = ListNode()
    assert got == want

def test_case31():
    solution = Solution()
    got = solution.mergeTwoLists(ListNode(1), ListNode(2))
    want = ListNode(1, ListNode(2))
    assert got == want
