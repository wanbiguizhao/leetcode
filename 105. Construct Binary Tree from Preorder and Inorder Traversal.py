# Definition for a binary tree node.
from pickletools import read_uint8
from typing import Optional ,List 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None 
        root_node_val=preorder[0]
        root_node=TreeNode(val=root_node_val)
        root_node_index_inorder=inorder.index(root_node_val)
        root_node.left=self.buildTree(preorder[1:1+root_node_index_inorder] ,inorder[0:root_node_index_inorder] )# 构建左右两个子树
        root_node.right=self.buildTree( preorder[1+root_node_index_inorder:], inorder[root_node_index_inorder+1:])# 构建左右两个子树
        return root_node
