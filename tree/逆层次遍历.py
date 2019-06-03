# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """                                                   
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        result,cur=[],[root]
        while cur:
            next_level,vals=[],[]
            for node in cur:
                vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            cur=next_level
            result.append(vals)
        return result[::-1]
