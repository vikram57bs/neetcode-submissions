# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        ino_map={val:i for i,val in enumerate(inorder)}
        pre_idx=0
        def df(left,right):
            nonlocal pre_idx
            if(left>=right):
                return
            val=preorder[pre_idx]
            pre_idx+=1
            mid=ino_map[val]
            root=TreeNode(val)
            root.left=df(left,mid)
            root.right=df(mid+1,right)
            return root
        return df(0,len(inorder))