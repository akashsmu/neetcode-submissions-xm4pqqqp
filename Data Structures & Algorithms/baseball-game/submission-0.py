class Solution:
    def calPoints(self, operations: List[str]) -> int:
        value = []
        for i in range(len(operations)):
            if operations[i] == "C":
                value.pop()
            elif operations[i] == "D":
                value.append(value[-1] * 2)
            elif operations[i] == "+":
                if len(value) >= 2:
                    value.append(value[-1] + value[-2])
            else:
                value.append(int(operations[i]))
        
        return sum(value)