class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        score=[]
        top=-1
        for i in range(len(operations)):
            if operations[i].lstrip("-").isdigit():
                score.append(int(operations[i]))
                top+=1
            elif operations[i]=="C":
                score.pop()
                top-=1
            elif operations[i]=="D":
                score.append(2*score[top])
                top+=1
            elif operations[i]=="+":
                score.append(score[top]+score[top-1])
                top+=1
        return sum(score)