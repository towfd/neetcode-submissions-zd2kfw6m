class Solution:
    def trap(self, height: List[int]) -> int:
        # 給定兩個指針 一個從左邊走 一個從右邊走
        # 每一步時判斷左右指針哪一個比較低 以比較低的開始往前走 若相同 統一由左邊開始走
        # 往前走時 較矮的那一方會進行結算，結算規則是，若遇到目前的height比較低 則加總 height - current_height 若比較高 則height = current_height
        lindex, rindex = 0, len(height) - 1
        lheight, rheight = height[lindex], height[rindex]
        asum = 0
        while lindex < rindex:
            if lheight <= rheight:
                lindex += 1
                if height[lindex] >= lheight:
                    lheight = height[lindex]
                else:
                    asum += lheight - height[lindex]
            else:
                rindex -= 1
                if height[rindex] >= rheight:
                    rheight = height[rindex]
                else:
                    asum += rheight - height[rindex]
        return asum
            
