#Definition for a binary tree node.
from typing import Optional 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # 使用临时节点的方法
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True 
        self.ans=True
        self.xnode=None
        self.mid_order(root)
        return self.ans
    def mid_order(self,root):
        if not root or not self.ans:
            return  
        self.mid_order(root.left)
        if not self.ans:
            return 
        # 根节点
        if not self.xnode:
            self.xnode=root
        else:
            if self.xnode.val>=root.val:
                self.ans=False
            else:
                self.xnode=root
        self.mid_order(root.right)
class Solution1:
    # 使用堆栈的方法
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True 
        self.ans=True
        node_stack=[]
        self.mid_order(root,node_stack)
        return self.ans
    def mid_order(self,root,node_stack):
        if not root or not self.ans:
            return  
        self.mid_order(root.left,node_stack)
        if not self.ans:
            return
        # 根节点
        if not node_stack:
            node_stack.append(root.val)
        else:
            if node_stack[-1]>=root.val:
                self.ans=False
            else:
                node_stack.pop(-1)
                node_stack.append(root.val)
        self.mid_order(root.right,node_stack)

# 使用pop的方式，的确比使用对象指针的方式效率低。
# 中序遍历，当前节点要比上一个节点大。 ==的情况属于错
# 