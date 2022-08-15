
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
#         m, n = len(matrix), len(matrix[0])
#         res = []
#         l, r = 0, n
#         t, b = 0, m 

#         while l<r and t<b:  # till matrxi is not filled/traveresed, spirally

#             # 1. fill TOP row (ie from left -> right)
#             for j in range(l, r):
#                 res.append(matrix[t][j])
#             t += 1 # update next top row

#             # 2. fill RIGHT col (ie from top -> down)
#             for i in range(t, b):
#                 res.append(matrix[i][r-1])
#             r -= 1 # update right boundary

#             if not (l < r and t < b):  # Single row or single col
#                 break 

#             # 3. fill BOTTOM row (ie from right -> left)
#             for j in range(r-1, l-1, -1):
#                 res.append(matrix[b-1][j])
#             b -= 1 # update next bottom row

#             # 4. fill LEFT col (ie from bottom -> top)
#             for i in range(b-1, t-1, -1):
#                 res.append(matrix[i][l])
#             l += 1 # update left boundary

#         return res 
        
        
        
        
        m=len(matrix)
        n=len(matrix[0])
        res=[]
        l=t=0
        r=n
        d=m
        while l<r and t<d:
            for i in range(l,r):
                res.append(matrix[t][i])
            t+=1
            for i in range(t,d):
                res.append(matrix[i][r-1])
            r-=1
            if not (l < r and t < d):  # Single row or single col
                 break 

            for i in range(r-1,l-1,-1):
                res.append(matrix[d-1][i])
            d-=1
            for i in range(d-1,t-1,-1):
                res.append(matrix[i][l])
            l+=1
        return res
            
   
