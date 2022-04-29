from typing import Optional ,List 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_queue=[]
        ans =[]
        if not root:
            return ans 
        level_queue.append(root)
        while level_queue:
            tmp_queue=[]
            tmp_ans=[]
            for node in level_queue:
                tmp_ans.append(node.val)
                if node.left:
                    tmp_queue.append(node.left)
                if node.right:
                    tmp_queue.append(node.right)
            ans.append(tmp_ans)
            level_queue=tmp_queue
        return ans 