from typing import List 
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans=root.val
        left_ans=self.maxChildrenPathSum(root.left)
        right_ans=self.maxChildrenPathSum(root.right)
        self.ans=max([self.ans,left_ans+root.val,right_ans+root.val,left_ans+right_ans+root.val])
        return self.ans 
    def maxChildrenPathSum(self,root:TreeNode):
        if not root:
            return 0 
        right_ans=left_ans=0
        if root.left:
            left_ans=self.maxChildrenPathSum(root.left)
        if root.right:
            right_ans=self.maxChildrenPathSum(root.right) 
        #ans=max(ans,left_ans+right_ans+ans)
        return_ans=max([left_ans,right_ans,0])+root.val
        self.ans=max([self.ans,return_ans,left_ans+right_ans+root.val])
        return return_ans 
        


def testCase0(instance:Solution=Solution()):
    pass
def wrongCase0(instance:Solution=Solution()):
    pass
if __name__ =="__main__":
    testCase0()
    wrongCase0()