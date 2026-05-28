class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenDict = {}
        for i, num in enumerate(nums):
            complement = target - num

            if complement in seenDict:
                return [seenDict[complement], i]
            
            seenDict[num] = i
        