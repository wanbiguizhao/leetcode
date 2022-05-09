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

        left= self._get_lowest_ancestor(root.left,p,q)
        right=self._get_lowest_ancestor(root.right,p,q)
        if root.val     