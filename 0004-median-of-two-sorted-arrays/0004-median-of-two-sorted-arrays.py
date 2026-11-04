class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        res=[]
        i=j=0
        
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<=nums2[j]:
                res.append(nums1[i])
                i+=1
            else:
                res.append(nums2[j])
                j+=1
        res.extend(nums1[i:])
        res.extend(nums2[j:])
        m=len(res)
        if len(res)%2==0:
            return (res[m//2-1]+res[m//2])/2.0
        else:
            return float(res[m//2])