class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l=0
        h=len(nums)-1
        result=-1
        while l<=h:
            m=(l+h)//2
            if nums[m]==target:
                result=m
                break
            elif nums[m]<target:
                l=m+1
            else:
                h=m-1
        return result