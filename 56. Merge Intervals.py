from typing import List 
class Solution:
    def merge_bad(self, intervals: List[List[int]]) -> List[List[int]]:
        new_intervals=sorted(intervals)
        ans=[]
        index_i=index_j=0
        const_len=len(intervals)
        max_right=new_intervals[index_j][1]
        while index_j<const_len:
            if new_intervals[index_j][0]>max_right:
                ans.append(
                    [
                        new_intervals[index_i][0],
                        max_right
                    ]
                )
                max_right=new_intervals[index_j][1]
                index_i=index_j
            max_right=max(max_right,new_intervals[index_j][1])
            index_j+=1
        ans.append(
                    [
                        new_intervals[index_i][0],
                        max_right
                    ]
        )
        return ans 
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        new_intervals=sorted(intervals)
        ans=[]
        index_i=index_j=0
        const_len=len(intervals)
        max_right=new_intervals[index_j][1]
        while index_j<const_len:
            if not ans or ans[-1][1] < new_intervals[index_j][0]: 
                ans.append(
                    [
                        new_intervals[index_j][0],
                        new_intervals[index_j][1]
                    ]
                )
            ans[-1][1]=max(ans[-1][1],new_intervals[index_j][1] )
            index_j+=1
        return ans
if __name__ == "__main__":
    instance=Solution()
    # print(instance.merge(intervals = [[1,3],[2,6],[8,10],[15,18]]))
    # print(instance.merge(intervals = [[1,18]]))
    print(instance.merge(intervals = [[2,4],[1,5],[1,6],[2,14]]))