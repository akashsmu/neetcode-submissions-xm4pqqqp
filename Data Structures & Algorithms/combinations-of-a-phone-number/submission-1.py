class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_to_letter = {
            "1": "",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        if not len(digits): return []
        if len(digits) == 1: return list(num_to_letter[digits])

        res = [""]
        for digit in digits:
            tmp = []
            for curStr in res:
                for c in num_to_letter[digit]:
                    tmp.append(curStr+c)
            res = tmp
        return res

