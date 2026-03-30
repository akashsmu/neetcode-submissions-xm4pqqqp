class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}
        for st in strs:
            orderStr = str(sorted(st))
            if orderStr in anagram:
                anagram[orderStr].append(st)
            else:
                anagram[orderStr] = [st]
        
        return [value for key, value in anagram.items()]