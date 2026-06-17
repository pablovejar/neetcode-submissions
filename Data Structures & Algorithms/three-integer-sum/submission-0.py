class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        numsSorted = sorted(nums)
        answer = []
        for i in range(len(nums)):
            left = i+1
            right = len(nums)-1
            while left<right:
                s = numsSorted[i]+numsSorted[left]+numsSorted[right]
                if s > 0:
                    right -= 1
                elif s < 0:
                    left += 1
                else:
                    newTriplet = sorted([numsSorted[i], numsSorted[left], numsSorted[right]])
                    if newTriplet not in answer:
                        answer.append(newTriplet)
                    right -=1
                    left +=1

        return answer


        