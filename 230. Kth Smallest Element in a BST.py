from typing import Optional 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def _kth(root,k):
            if self.stop:
                return 
            if root.left:
                self.kthSmallest(root.left,k)
            if self.stop:
                return
            k-=1
            if k==0:
                self.ans=root.val
                self.stop=True
                return 
            if root.right:
                self.kthSmallest(root.right,k)
        self.ans=0
        self.stop=False
        _kth(root,k)

