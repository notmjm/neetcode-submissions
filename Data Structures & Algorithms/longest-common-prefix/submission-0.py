class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = strs[0]
        
        for i in range(1, len(strs)):
            j = 0
            while j < len(pre):
                if j >= len(strs[i]) or pre[j] != strs[i][j]:
                    pre = pre[:j]
                else:
                    j += 1
        
        return pre


        
        