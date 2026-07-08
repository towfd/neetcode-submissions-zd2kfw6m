# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 想法：建立一個linklist出來，
        # 對兩個list各自建立自己的指標
        # 針對目前的val較小的那個去跑
        # 直到list1_cur, list2_cur 跑完即結束
        # 回傳結果
        # 時間複雜度O(n + m)
        # 空間複雜度O(1)

        list1_cur = list1
        list2_cur = list2

        dummy = ListNode()
        cur = dummy
        while list1_cur and list2_cur:
            if list1_cur.val < list2_cur.val:
                cur.next = list1_cur
                list1_cur = list1_cur.next
            else:
                cur.next = list2_cur
                list2_cur = list2_cur.next
            cur = cur.next
        if list1_cur:
            cur.next = list1_cur
        elif list2_cur:
            cur.next = list2_cur

        return dummy.next