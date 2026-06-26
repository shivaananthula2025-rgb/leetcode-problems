# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result=[]
        def postorder(curr,result):
            if not curr:
                return
            postorder(curr.left,result)
            postorder(curr.right,result)
            result.append(curr.val)
        postorder(root,result)
        return result