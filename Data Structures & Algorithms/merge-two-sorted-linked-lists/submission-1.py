# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 遞迴
        # 思考：
        # 每次先對比目前的list中哪個數值比較小，當頭
        # 較小的再去將他下面的值去與另外一個陣列的去比較
        # 直到某一邊為空了，結束遞迴
        if not list1:
            return list2
        elif not list2:
            return list1

        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list2.next, list1)
            return list2
