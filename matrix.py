import collections
import numpy as np
class Solution:
    def diagonalSort(self, mat):
        m, n = len(mat), len(mat[0])
        d = collections.defaultdict(list)
        for i in range(m):
            for j in range(n):
                d[i-j].append(mat[i][j])
        for k in d:
            d[k].sort(reverse=1)
        for i in range(m):
            for j in range(n):
                mat[i][j] = d[i-j].pop()
        return mat
val=Solution()
n=int(input())
R=n
C=n
nums=list(map(int,input().split()))
matrix=np.array(nums).reshape(R,C)
print(val.diagonalSort(matrix))
