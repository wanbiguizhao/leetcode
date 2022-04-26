from typing import List 
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        const_m=len(matrix)
        const_n=len(matrix[0])
        const_len=const_n*const_m
        current_len=0

        left_bound=0
        right_bound=const_n-1
        up_bound=0
        down_bound=const_m-1
        ans=[]
        while left_bound<=right_bound and up_bound<=down_bound:
            i,j=up_bound,left_bound
            while  current_len<const_len and j<=right_bound:
                ans.append(matrix[i][j])
                j+=1
            current_len+=right_bound-left_bound+1
            up_bound+=1
            i,j=up_bound,right_bound
            while current_len<const_len and i<=down_bound:
                ans.append(matrix[i][j])
                i=i+1
            current_len+=down_bound-up_bound+1
            right_bound-=1
            i,j=down_bound,right_bound
            while current_len<const_len and j>=left_bound:
                ans.append(matrix[i][j])
                j=j-1
            current_len+=left_bound-right_bound+1
            down_bound-=1
            i,j=down_bound,left_bound
            while current_len<const_len and i>=up_bound:
                ans.append(matrix[i][j])
                i=i-1
            current_len+=down_bound-up_bound+1
            left_bound+=1
        return ans 
if __name__ == "__main__":
    instance=Solution()
    instance.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

            
        