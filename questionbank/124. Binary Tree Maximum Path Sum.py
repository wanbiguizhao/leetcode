# Definition for a binary tree node.
from turtle import right
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans=root.val 
        self._maxPathSum(root)
        return self.ans
    
    def _maxPathSum(self,root:TreeNode):
        if not root:
            return 0
        left_max_ans=max(self._maxPathSum(root.left),0)
        right_max_ans=max(self._maxPathSum(root.right),0)
        self.ans=max(left_max_ans+right_max_ans+root.val,self.ans) # 计算包含左子树，根节点的，右边子树的组合
            
        #leave_ans=max(left_max_ans,right_max_ans)
        return max([ 
            root.val+left_max_ans, # 肯定是包含根节点的
            root.val+right_max_ans,
        ])

        
