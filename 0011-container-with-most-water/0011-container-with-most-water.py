class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l,r=0,len(height)-1
        max_area=0
        area=0
        while l<r:
            area=min(height[l],height[r])*(r-l)
            max_area=max(area,max_area)
            if height[l]<height[r]:
                l+=1
            elif height[l]>height[r]:
                r-=1
            else:
                l+=1
        return max_area