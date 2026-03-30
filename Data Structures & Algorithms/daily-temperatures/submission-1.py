class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # res =[0] * len(temperatures)
        # for i in range(len(temperatures)):
        #     for j in range(i, len(temperatures)):
        #         if temperatures[j] > temperatures[i]:
        #             res[i] = j - i
        #             break
        # return res

        res = [0]*len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                temp, index = stack.pop()
                res[index] = i - index
            stack.append((temperatures[i],i))
        return res