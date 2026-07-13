# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 定義兩個指標
        # 指標1固定往前一步，指標2固定往前兩步
        # 若指標2走到null 回傳False, 若指標2碰到指標1，則回傳True，代表有cycle

        idx1 = head
        idx2 = head

        while idx2 and idx2.next:
            idx1 = idx1.next
            idx2 = idx2.next.next
            if idx2 == idx1:
                return True
        return False