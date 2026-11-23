class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l=0
        r=len(numbers)-1
        sum=0
        while l<r:
            sum=numbers[l]+numbers[r]
            if sum>target:
                r-=1    
                sum-=numbers[r]
            elif sum<target:
                l+=1
                sum-=numbers[l]
            else:
                return l+1,r+1
                break            