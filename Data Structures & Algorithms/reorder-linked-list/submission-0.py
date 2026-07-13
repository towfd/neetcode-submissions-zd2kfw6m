# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 給定兩個指標，指標1走一步 指標2走兩步
        # 當指標2走到盡頭時，指標1會剛好到中心點
        # 從中心點將這條linklist拆成兩條
        # 將後面的linklist做反轉
        # 反轉完畢後，將其交叉接回前面那條linklist
        # 時間複雜度O(n)
        # 空間複雜度O(1)

        idx1 = head
        idx2 = head
        
        while idx2 and idx2.next:
            idx1 = idx1.next
            idx2 = idx2.next.next
        
        idx2 = idx1.next
        idx1.next = None
        idx1 = head
        
        pre = None
        cur = idx2
        
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp

        while idx1 and pre:
            idx1_tmp = idx1.next
            pre_tmp = pre.next

            idx1.next = pre
            pre.next = idx1_tmp
            
            idx1 = idx1_tmp
            pre = pre_tmp
