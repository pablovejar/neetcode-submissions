class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxConsecutive = 0
        possibleStarts = set()

        for num in numSet:
            if num-1 not in numSet: #possibleStart
                possibleStarts.add(num)
        
        for start in possibleStarts:
            nextNumber = start + 1
            length = 1
            while nextNumber in numSet:
                length +=1
                nextNumber +=1
            maxConsecutive = max(maxConsecutive,length)
        
        return maxConsecutive
