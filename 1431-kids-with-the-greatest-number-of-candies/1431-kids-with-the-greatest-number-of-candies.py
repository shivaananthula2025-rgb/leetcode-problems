class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        res=[]
        m=max(candies)
        for i in range(len(candies)):
            if candies[i]+extraCandies>=m:
                res.append(True)
            else:
                res.append(False)

        return res