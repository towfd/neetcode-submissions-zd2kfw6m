# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 使用Recursion解
        # 運作解釋
        # 假設input = [1, 2, 3]
        # 這時候linklist = 1 -> 2 -> 3 -> None
        # 程式不會馬上反轉 1，而是先一路呼叫到 3
        # 3 是最後一個節點，觸發終止條件，直接回傳 3 當作 new_head
        # 退回到 2 的那一層：2.next 是 3，讓 2.next.next = 2 就是讓 3 指向 2。然後 2.next = None
        # 退回到 1 的那一層：1.next 是 2，所以 1.next.next = 1 就是讓 2 指向 1。然後 1.next = None
        # 時間複雜度O(n)
        # 空間複雜度O(n)
        if not head or not head.next:
            return head

        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return new_head