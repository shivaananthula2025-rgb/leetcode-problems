class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        seen={}
        l=[]
        for i in arr:
            seen[i]=seen.get(i,0)+1
        
        for j in seen.values():
            l.append(j)
        return len(l)==len(set(l))
        