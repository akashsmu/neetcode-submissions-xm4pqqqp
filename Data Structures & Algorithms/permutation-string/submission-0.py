class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counterS1 = {}
        for char in s1:
            counterS1[char] = counterS1.get(char,0) + 1

        for i in range(len(s2)):
            slicedStr = s2[i:i+len(s1)]
            counterS2 = {}
            for char in slicedStr:
                counterS2[char] = counterS2.get(char,0) + 1
            if counterS2 == counterS1:
                return True
        
        return False
            
