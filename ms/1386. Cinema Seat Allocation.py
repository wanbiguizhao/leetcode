from typing import List 
from collections import defaultdict
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        # 因为有边栏的存在，每行最多有2个group，来自于座位号：2,3,4,5,6,7,8,9 
        # reservedSeats是否一定可以按照行号n，进行排序，然后按照行进行分组。
        # 可能的四组的作为组合是[2,3,4,5,],[4,5,6,7],[6,7,8,9]
         
        reservedRowSeatsInfo=defaultdict(lambda : [False]*10)
        def judgeFourGroupCount(seats:List):
            from2to5=1 
            from4to7=1 
            from6to9=1
            for col_x in range(10):
                if seats[col_x]:
                    col_x=col_x+1
                    if col_x>=2 and col_x<=5 and from2to5==1:
                        from2to5=0
                    if col_x>=4 and col_x<=7 and from4to7==1:
                        from4to7=0
                    if col_x>=6 and col_x<=9 and from6to9==1:
                        from6to9=0
            if from2to5+from4to7+from6to9==0:
                return 0 
            elif from2to5+from4to7+from6to9==3:
                return 2 
            else:
                return 1
        for seatinfo in reservedSeats:
            reservedRowSeatsInfo[seatinfo[0]][seatinfo[1]-1]=True 
        ans=0
        for i in range(1,n+1):
            if i not in reservedRowSeatsInfo:
                ans+=2
            else:
                ans+=judgeFourGroupCount(reservedRowSeatsInfo[i])      
        return ans 
if __name__=="__main__":
    instance=Solution()
    instance.maxNumberOfFamilies( n = 2, reservedSeats = [[1,5],[2,1],[2,10]])