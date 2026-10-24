class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        p = []
        ans = 0
        for i in s:
            if i == "(":
                p.append(i)
            else:
                if p:
                    p.pop()
                else:
                    ans += 1
        return ans + len(p)