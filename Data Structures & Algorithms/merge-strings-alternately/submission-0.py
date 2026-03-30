class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1len = len(word1)
        w2len = len(word2)
        minlen = min(w1len, w2len)

        l,r = 0,0
        res = ""
        while l < minlen:
            res += word1[l] + word2[r]
            l+=1
            r+=1
        
        if l < w1len:
            res += word1[l:]
        if r < w2len:
            res += word2[r:]
        return res
