class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        seen={}
        c=0
        for i in nums:
            if i in seen:
                seen[i]+=1
            else:
                seen[i]=1
        for j in seen:
            if seen[j]>n//2:
                return j