class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ##prefix
        prefix = []
        prefixProduct = 1
        prefix.append(prefixProduct)
        j = 0
        while j < len(nums) - 1:
            prefixProduct *= nums[j]
            prefix.append(prefixProduct)
            j += 1

        ##suffix
        suffix = []
        suffixProduct = 1
        suffix.append(suffixProduct)
        j = len(nums)-1
        while j > 0:
            suffixProduct *= nums[j]
            suffix.append(suffixProduct)
            j -=1

        result = [prefix[i]*list(reversed(suffix))[i] for i in range(len(nums))]
        return result