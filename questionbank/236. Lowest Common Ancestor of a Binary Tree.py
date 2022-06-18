from time import sleep
from cv2 import sepFilter2D


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans=None 

        self._get_lowest_ancestor(root,p,q)
        return self.ans
    def _get_lowest_ancestor(self,root:'TreeNode',p:'TreeNode',q:'TreeNode'):
        # 使用数学计数的方法进行判断
        if not root:
            return 0

        left= self._get_lowest_ancestor(root.left,p,q)
        right=self._get_lowest_ancestor(root.right,p,q)
        mid=0
        if root.val==p.val or root.val==q.val:
            mid=1
        if mid+left+right>=2:
            self.ans=root 
            return 0
        else:
            return mid+left+right
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 反转指针法
        self.ans=None 
        pass 