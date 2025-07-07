from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ListNode):
            return False

        current1, current2 = self, other
        while current1 and current2:
            if current1.val != current2.val:
                return False
            current1 = current1.next
            current2 = current2.next

        return current1 is None and current2 is None


class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy

        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        if l1 or l2:
            current.next = l1 if l1 else l2

        return dummy.next



if __name__ == "__main__":
    solution = Solution()
    l3 = solution.mergeTwoLists(
        ListNode(2, ListNode(7)),
        ListNode(1, ListNode(3))
    )

    while l3:
        if l3:
            print(l3.val)
            l3 = l3.next
