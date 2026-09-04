class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        totals = {}

        for s in strs:
            combos = [0] * 26
            for c in s:
                combos[ord(c) - ord('a')] += 1
            
            key = tuple(combos)

            if key not in totals:
                totals[key] = []
            totals[key].append(s)
        return list(totals.values())