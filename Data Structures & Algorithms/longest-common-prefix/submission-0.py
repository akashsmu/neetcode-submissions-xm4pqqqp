class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minlenStr = min(strs, key = lambda x : len(x))
        strs.remove(minlenStr)

        res = ""
        for i in range(len(minlenStr)):
            char = minlenStr[i]
            for st in strs:
                if st[i] != char:
                    return res
            res += char 

        return res