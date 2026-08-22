class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        gp=0
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                if nums[i]==nums[j] and i<j:
                    gp+=1
        return gp