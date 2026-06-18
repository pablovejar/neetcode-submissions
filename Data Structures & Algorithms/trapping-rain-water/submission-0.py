class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 1: return 0

        totalWater = 0
        i = 0
        j = len(height)-1
        maxLeft = height[i]
        maxRight = height[j]
        while i<j:
            if maxLeft <= maxRight :
                i += 1
                maxLeft = max(maxLeft,height[i])
                totalWater += maxLeft-height[i]
            else:
                j -=1
                maxRight = max(maxRight, height[j])
                totalWater += maxRight-height[j]
        return totalWater
            
                                   