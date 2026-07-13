# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 將每個節點放入list中
        # 設定兩個指標 一左一右
        # 從最左邊的開始 做指標往前+1 右指標往後-1 並依序加入
        # 直到指標碰到為止，將最後指標的next設置為None
        # 時間複雜度O(n)
        # 空間複雜度O(n)
        if not head:
            return

        node_list = []
        cur = head
        while cur:
            node_list.append(cur)
            cur = cur.next

        l_idx, r_idx = 0, len(node_list) - 1
        while l_idx < r_idx:
            node_list[l_idx].next = node_list[r_idx]
            l_idx += 1

            if l_idx == r_idx:
                break

            node_list[r_idx].next = node_list[l_idx]
            r_idx -= 1

        node_list[l_idx].next = None
            

