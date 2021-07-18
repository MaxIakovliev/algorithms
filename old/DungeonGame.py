class Solution:
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        if dungeon is None or len(dungeon) == 0:
            return 0

        m = len(dungeon)
        n = len(dungeon[0])

        hp = [[0 for j in range(n)] for i in range(m)]

        hp[m-1][n-1] = abs(dungeon[m-1][n-1])+1 if dungeon[m-1][n-1] < 0 else 1

        for j in range(n-2,-1,-1):
              
            need = hp[m-1][j+1] - dungeon[m-1][j]
          
            if need <= 0:
                hp[m-1][j] = 1
            else:
                hp[m-1][j] = need
        for i in range(m-2, -1, -1):
            need = hp[i+1][n-1]-dungeon[i][n-1]
            if need <= 0:
                hp[i][n-1] = 1
            else:
                hp[i][n-1] = need

        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                need = min(hp[i+1][j], hp[i][j+1]) - dungeon[i][j]
                if need <= 0:
                    hp[i][j] = 1
                else:
                    hp[i][j] = need

        return hp[0][0]


    def calculateMinimumHP2(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        if not dungeon or len(dungeon) == 0:
            return 0
        
        m = len(dungeon)
        n = len(dungeon[0])
        
        hp = [ [ 0 for j in range(n) ] for i in range(m) ]
       
        hp[m-1][n-1] = abs(dungeon[m-1][n-1]) + 1 if dungeon[m-1][n-1] < 0 else 1

        for j in range(n-2,-1,-1):
          
            need = hp[m-1][j+1] - dungeon[m-1][j]
          
            if need <= 0:
                hp[m-1][j] = 1
            else:
                hp[m-1][j] = need
        for i in range(m-2,-1,-1):
            need = hp[i+1][n-1] - dungeon[i][n-1]
            if need <= 0:
                hp[i][n-1] = 1
            else:
                hp[i][n-1] = need

        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                need = min(hp[i+1][j], hp[i][j+1]) - dungeon[i][j]
                if need <= 0:
                    hp[i][j] = 1
                else:
                    hp[i][j] = need
        
        return hp[0][0]

c=Solution()
print(c.calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]]))
