# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count=0
        result=None
        def sf(node):
            nonlocal count,result
            if node is None or result is not None:
                return
            sf(node.left)
            count+=1
            if count==k:
                result=node.val
                return
            sf(node.right)
        sf(root)
        return result