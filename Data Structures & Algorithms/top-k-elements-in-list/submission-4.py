class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}

        for n in nums:
            counter[n] = 1 + counter.get(n,0)
        
        buckets = [set() for _ in range(len(nums)+1)]

        for n, qty in counter.items():
            buckets[qty].add(n)

        result = []

        for buc in reversed(buckets):
            for num in buc:
                result.append(num)

                if len(result) == k:
                    return result
