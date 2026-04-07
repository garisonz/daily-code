class Solution:
    def calPoints(self, operations: List[str]) -> int:
        temp = []
        total = 0
        for op in operations:
            if op == '+':
                temp.append(temp[-1] + temp[-2])
            elif op == 'D':
                temp.append(temp[-1] * 2)
            elif op == 'C':
                temp.pop()
            else:
                temp.append(int(op))

        for i in temp:
            total += i
        
        return total