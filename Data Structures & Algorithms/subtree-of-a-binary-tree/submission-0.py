# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if(root is None):
            return False
        elif(root.val==subRoot.val):
            a=self.checkSame(root,subRoot)
            if(a):
                return True
            else:
                c=self.isSubtree(root.left,subRoot)
                d=self.isSubtree(root.right,subRoot)
                if(c or d):
                    return True
                else:
                    return False
        else:
            c=self.isSubtree(root.left,subRoot)
            d=self.isSubtree(root.right,subRoot)
            if(c or d):
                return True
            else:
                return False

        return False

    def checkSame(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if(root1 and root2):
            if(root1.val!=root2.val):
                return False
            left=self.checkSame(root1.left,root2.left)
            right=self.checkSame(root1.right,root2.right)
            return left and right
        elif root1 is None and root2 is None:
            return True
        else:
            return False