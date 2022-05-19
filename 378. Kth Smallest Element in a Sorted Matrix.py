from typing import List 
from heapq import heappush,heappop
class Solution:
    def kthSmallest(self, matrix, k):
        n, beg, end = len(matrix), matrix[0][0], matrix[-1][-1]
        # 就只找到k就可以了。
        def check(m):
            i, j, cnt = 0, n-1, 0
            for i in range(n):
                while j >= 0 and matrix[i][j] > m: j -= 1
                cnt += (j + 1)
            return cnt
         
        while beg < end:
            mid = (beg + end)//2
            if check(mid) < k:
                beg = mid + 1
            else:
                end = mid
        a=[]
        
        return beg
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])  # For general, the matrix need not be a square
        minHeap = []  # val, r, c
        for r in range(min(k, m)):
            heappush(minHeap, (matrix[r][0], r, 0))

        ans = -1  # any dummy value
        for i in range(k):
            ans, r, c = heappop(minHeap)
            if c+1 < n: heappush(minHeap, (matrix[r][c + 1], r, c + 1))# 检查是否存在越界的情况
        return ans