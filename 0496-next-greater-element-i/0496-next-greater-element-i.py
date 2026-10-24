class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack=[]
        d={}
        for i in nums2:
            while stack and i>stack[-1]:
                t=stack.pop()
                d[t]=i
            stack.append(i)
        while len(stack)!=0:
            t=stack.pop()
            d[t]=-1
        res=[]
        for i in nums1:
            res.append(d.get(i,-1))
        return res
