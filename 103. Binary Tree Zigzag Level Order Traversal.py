from typing import Optional ,List 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        reverse_flag=False  # 初始值特别重要
        level_queue=[]
        ans =[]
        if not root:
            return ans 
        level_queue.append(root)
        while level_queue:
            tmp_queue=[]
            tmp_ans=[]
            for node in level_queue:
                #tmp_ans.append(node.val)
                if reverse_flag: # 使用reverse_flag判断tmp_ans 的添加方向，比翻转tmp_ans要高效一些
                    tmp_ans.insert(0,node.val)
                else:
                    tmp_ans.append(node.val)
                if node.left:
                    tmp_queue.append(node.left)
                if node.right:
                    tmp_queue.append(node.right)
            # if reverse_flag:
            #     ans.append(tmp_ans[::-1]) # revered 函数不要乱用。 注意翻转的是结果，不是tmp_queue的顺序
            # else:
            #     ans.append(tmp_ans)
            ans.append(tmp_ans)
            level_queue=tmp_queue
            reverse_flag=not reverse_flag
        return ans 
if __name__ == "__main__":
    instance=Solution()
    instance.zigzagLevelOrder