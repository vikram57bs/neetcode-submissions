# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue=deque([root])
        result=[]
        while queue:
            level=[]
            leng=len(queue)
            for i in range(leng):
                a=queue.popleft()
                level.append(a.val)
                if(a.left):
                    queue.append(a.left)
                if(a.right):
                    queue.append(a.right)
            result.append(level)
        return result