class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        uni=[]
        top=-1
        for i in range(len(s)):
            if top==-1:
                uni.append(s[i])
                top+=1
            elif s[i]==uni[top]:
                uni.pop()
                top-=1
            else:
                uni.append(s[i])
                top+=1
        return "".join(uni)