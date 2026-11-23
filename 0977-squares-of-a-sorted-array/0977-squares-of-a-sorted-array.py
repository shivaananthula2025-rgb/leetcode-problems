class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sq=[0]*len(nums)
        l,r=0,len(nums)-1
        pos=len(nums)-1
        while l <= r:
            left = nums[l] ** 2
            right = nums[r] ** 2
            if left > right:
                sq[pos] = left
                l += 1
            else:
                sq[pos] = right
                r -= 1
            pos -= 1
        return sq
