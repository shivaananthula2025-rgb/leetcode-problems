class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen={}
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen[nums[i]]=0
            seen[nums[i]]+=1
        for key in seen:
            if seen[key]==1:
                return key