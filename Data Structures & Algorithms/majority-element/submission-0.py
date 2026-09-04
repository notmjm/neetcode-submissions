class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elems = {}

        for c in nums:
            elems[c] = elems.get(c, 0) + 1
        
        for e in elems:
            if elems[e] > len(nums) / 2:
                return e