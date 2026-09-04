class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left=0
        right=0
        count=0
        m_count=0
        while right<len(s):
            if s[right] in "aeiouAEIOU":
                count+=1
            
            if right-left+1==k:
                m_count=max(count,m_count)
                if s[left] in "aeiouAEIOU":
                    count-=1
                left+=1
            right+=1
        return m_count
        
                