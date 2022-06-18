from typing import Optional 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # 递归方式
        # 找到停止递归的方法。
        def _kth(root):
            if root.left:
                _kth(root.left)
            if self.stop:
                return
            self.k-=1
            if self.k==0:
                self.ans=root.val
                self.stop=True
                return 
            if root.right:
                _kth(root.right)
        self.ans=0
        self.stop=False
        self.k=k
        _kth(root)
        return self.ans
