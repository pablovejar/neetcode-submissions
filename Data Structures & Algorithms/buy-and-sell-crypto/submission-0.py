class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxValue = 0
        minSelling = prices[0]

        for i in range(1, len(prices)):
            minSelling = min(minSelling, prices[i])
            maxValue = max(maxValue, prices[i]-minSelling)


        return maxValue

        