class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen={}
        total=0
        for i in nums:
            seen[i]=seen.get(i,0)+1
        for j,k in seen.items():
            if k==1:
                total+=j
        return total