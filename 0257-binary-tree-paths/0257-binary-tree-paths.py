# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        result=[]
        def dfs(node,curr_path):
            if not node:
                return
            if curr_path:
                curr_path+="->"+str(node.val)
            else:
                curr_path=str(node.val)
            if not node.left and not node.right:
                result.append(curr_path)
                return 
            dfs(node.left,curr_path)
            dfs(node.right,curr_path)
        dfs(root,"")
        return result