from collections import defaultdict
from typing import List,Optional 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        tree_cache_parent_child=defaultdict(lambda: [0,0])
        tree_cache_child_parent=defaultdict()
        for desc in descriptions:
            parent, child, isLeft=desc
            tree_cache_parent_child[parent][isLeft]=child
            tree_cache_child_parent[child]=parent
        # find root node 
        root_node=list(set(tree_cache_parent_child.keys())-set(tree_cache_child_parent.keys()))[0]
        while True:
            if parent not in  tree_cache_child_parent:
                root_node=parent
                break
            parent=tree_cache_child_parent[parent]
        ans = []
        root_tree_node=TreeNode(root_node)
        queue=[root_tree_node]
        while queue:
            tmp_queue=[]
            for node in queue:
                ans.append(node)
                if node :
                    right,left=tree_cache_parent_child[node.val]
                    if left:
                        node.left=TreeNode(left)                   
                    tmp_queue.append(node.left)
                    if right:
                        node.right=TreeNode(right)  
                    tmp_queue.append(node.right)
            queue=tmp_queue
        return root_tree_node
        DOWN_LIMIT=len(ans)-1
        while not ans[DOWN_LIMIT]:
            DOWN_LIMIT-=1
        return ans[:DOWN_LIMIT+1]

if __name__=="__main__":
    solution=Solution()
    solution.createBinaryTree([[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]])
    solution.createBinaryTree([[1,2,1],[2,3,0],[3,4,1]])
