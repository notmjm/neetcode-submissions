class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elems = {}
        maxFreq = len(nums)//2

        for c in nums:
            elems[c] = elems.get(c, 0) + 1
        
        for e in elems:
            if elems[e] > maxFreq:
                return e