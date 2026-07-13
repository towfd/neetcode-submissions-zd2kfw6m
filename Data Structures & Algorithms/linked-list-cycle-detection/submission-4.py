# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 用一個hashtable紀錄走過的值
        # 若下一個查詢到相同的值，回傳index，若下一個是null 回傳 -1
        cur_seen = set()
        cur = head
        while cur:
            if cur in cur_seen:
                return True
            cur_seen.add(cur)
            cur = cur.next

        return False