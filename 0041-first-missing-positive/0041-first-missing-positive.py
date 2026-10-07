class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j=1
        nums.sort()
        for i in range(len(nums)):
            if nums[i]==j:
                j+=1
        return j