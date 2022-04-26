from typing import List 
class Solution:
    def spiralOrder_1(self, matrix: List[List[int]]) -> List[int]:
        const_m=len(matrix)
        const_n=len(matrix[0])
        const_len=const_n*const_m
        left_bound=0
        right_bound=const_n-1
        up_bound=0
        down_bound=const_m-1
        ans=[]
        while left_bound<=right_bound and up_bound<=down_bound:
            i,j=up_bound,left_bound
            while  len(ans)!=const_len and j<=right_bound:
                ans.append(matrix[i][j])
                j+=1
            up_bound+=1
            i,j=up_bound,right_bound
            while len(ans)!=const_len and i<=down_bound:
                ans.append(matrix[i][j])
                i=i+1
            right_bound-=1
            i,j=down_bound,right_bound
            while len(ans)!=const_len and j>=left_bound:
                ans.append(matrix[i][j])
                j=j-1
            down_bound-=1
            i,j=down_bound,left_bound
            while len(ans)!=const_len and i>=up_bound:
                ans.append(matrix[i][j])
                i=i-1
            left_bound+=1
        return ans
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def check(i,j):
            if i<0 or i>=const_m or j<0 or j>=const_n or matrix[i][j]=="*":
                return False
            return True 
        const_m=len(matrix)
        const_n=len(matrix[0])
        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        ans=[]
        i,j=0,0
        direction_index=0
        while check(i,j):
            ans.append(matrix[i][j])
            matrix[i][j]="*"
            direction=directions[direction_index]
            i,j=i+direction[0],j+direction[1]
            if not check(i,j):
                i,j=i-direction[0],j-direction[1] # 回退
                direction_index=(direction_index+1)%4 # 换一个方向走。
                direction=directions[direction_index]
                i,j=i+direction[0],j+direction[1]
        return ans 



if __name__ == "__main__":
    instance=Solution()
    instance.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

            
        