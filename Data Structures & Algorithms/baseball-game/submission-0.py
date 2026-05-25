class Solution:
    def calPoints(self, operations: List[str]) -> int:
        resultArr = []
        for i in operations:
            if i == "+":
                resultArr.append(resultArr[-1] + resultArr[-2])
            elif i == "D":
                resultArr.append(2*resultArr[-1])
            elif i == 'C':
                resultArr.pop()
            else:
                resultArr.append(int(i))
            
        return sum(resultArr)