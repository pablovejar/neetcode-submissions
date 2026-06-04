class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxConsecutive = 0

        for num in numSet:
            if num-1 not in numSet: #possibleStart
                nextNumber = num + 1
                length = 1
                while nextNumber in numSet:
                    length +=1
                    nextNumber +=1
                maxConsecutive = max(maxConsecutive,length)
        
        return maxConsecutive
