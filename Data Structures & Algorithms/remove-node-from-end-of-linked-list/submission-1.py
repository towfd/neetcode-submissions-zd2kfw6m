# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create Two Pointers -> slow pointer and quick pointer.
        # First, the quick pointer moves n + 1 steps ahead.
        # Second, both pointers move forward together until the quick pointer reaches the end (None).
        # Because there is an n + 1 gap between them, when the quick pointer reaches the end,
        # the slow pointer will land exactly on the node BEFORE the target node.
        # Finally, remove the target node by updating slow.next, and return dummy.next.
        # Time complexity => O(N)
        # Space complexity => O(1)

        dummy = ListNode(0)
        dummy.next = head

        slow = dummy
        quick = dummy

        for _ in range(n + 1):
            quick = quick.next

        while quick:
            slow = slow.next
            quick = quick.next

        slow.next = slow.next.next
        return dummy.next