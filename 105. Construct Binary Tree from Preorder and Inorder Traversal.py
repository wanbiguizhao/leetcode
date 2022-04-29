# Definition for a binary tree node.
from logging import root
from pickletools import read_uint8
from typing import Optional ,List 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree_1(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None 
        root_node_val=preorder[0]
        root_node=TreeNode(val=root_node_val)
        root_node_index_inorder=inorder.index(root_node_val)
        root_node.left=self.buildTree(preorder[1:1+root_node_index_inorder] ,inorder[0:root_node_index_inorder] )# 构建左右两个子树
        root_node.right=self.buildTree( preorder[1+root_node_index_inorder:], inorder[root_node_index_inorder+1:])# 构建左右两个子树
        # python的数组冒号机制，保证了即使root_node_index_inorder存在越界的情况，也不会数组异常。
        return root_node
    # 通过索引进行区分左右两个子树的范围。
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def _buildTree(preorder_left,preorder_right,inorder_left,inorder_right):
            if preorder_left>preorder_right:
                return None 
            elif preorder_left==preorder_right:
                return TreeNode(val=preorder[preorder_left])
            else:
                # 22:30 开始尝试使用新的方法，现在23:26了，该开始花了半个小时，被打断一下一个小时过去了。
                root_node_val=preorder[preorder_left]
                root_node_index_inorder=inorder.index(root_node_val)
                left_tree_len=root_node_index_inorder-inorder_left
                root_node=TreeNode(val=root_node_val)
                root_node.left=_buildTree(
                                        preorder_left+1,
                                        preorder_left+1+left_tree_len-1,
                                        inorder_left,
                                        root_node_index_inorder-1,
                                        )
                root_node.right=_buildTree(
                    preorder_left+1+left_tree_len+1,
                    preorder_right,
                    root_node_index_inorder+1,
                    inorder_right
                )
                return root_node
        return _buildTree(0,len(preorder)-1,0,len(inorder)-1)