"""
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other 
cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith 
city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

 

Example 1:


Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
"""

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:        
        provinces, tmp, s = 0, set(), set(range(len(isConnected)))
        while s:                
            tmp.add(s.pop())
            provinces += 1    
            
            while tmp:
                i = tmp.pop()
                for j in list(s):
                    if isConnected[i][j]:
                        tmp.add(j)
                        s.remove(j)
        return provinces


