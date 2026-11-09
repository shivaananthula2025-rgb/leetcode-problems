class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=s.strip()
        w=l.split()
        return len(w[-1])