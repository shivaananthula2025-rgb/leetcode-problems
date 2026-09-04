class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left=0
        right=0
        s=0
        min_length=float('inf')
        while right<len(nums):
            s+=nums[right]
            while s>=target:
                min_length=min(min_length,right-left+1)
                s-=nums[left]
                left+=1
            right+=1
        if min_length==float('inf'):
            return 0
        else:
            return min_length