# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        a=[]
        b=[]
        def preorder(root,r):
            if root is None:
                r.append(None)
                return
            r.append(root.val)
            preorder(root.left,r)
            preorder(root.right,r)
        preorder(p,a)
        preorder(q,b)
        if a==b:
            return True
        return False
        
