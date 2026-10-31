class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        f=[]
        s=""
        for i in range(len(digits)):
            s=s+str(digits[i])
        num=int(s)+1
        n=str(num)
        for j in range(len(n)):
            f.append(int(n[j]))
        return f