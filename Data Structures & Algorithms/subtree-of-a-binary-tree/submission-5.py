# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False

        if root.val == subRoot.val and self.checkSame(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def checkSame(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if root1 and root2:
            if root1.val != root2.val:
                return False

            left = self.checkSame(root1.left, root2.left)
            right = self.checkSame(root1.right, root2.right)

            return left and right

        elif root1 is None and root2 is None:
            return True
        
        else:
            return False