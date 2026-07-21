# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Brute Force
        # ADD the head's value into a list
        # remove the nth value
        # return the list
        # Time complexity => O(n)
        # Space Complexity => O(n)
        
        cur = head
        nodes = []
        while cur:
            nodes.append(cur)
            cur = cur.next

        target_idx = len(nodes) - n

        if target_idx == 0:
            return head.next
        
        prev_node = nodes[target_idx - 1]
        prev_node.next = prev_node.next.next

        return head
