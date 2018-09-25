class Solution:
    """
    https://leetcode.com/problems/keys-and-rooms/description/
    """
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited=set()
        keys=[]
        if rooms is None or len(rooms)==0:
            return False
        for key in rooms[0]:
            keys.append(key)
        visited.add(0)

        while len(keys)>0:
            curKey=keys[0]
            del keys[0]
            if curKey in visited:
                continue
            for key in rooms[curKey]:
                keys.append(key)
            visited.add(curKey)

        if len(visited)<len(rooms):
            return False
        return True

            




                

        
        
if __name__=="__main__":
    c=Solution()
    print(c.canVisitAllRooms([[1],[2],[3],[]])) #True
    print(c.canVisitAllRooms([[1,3],[3,0,1],[2],[0]])) #False

        