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

            
    def canVisitAllRooms2(self, rooms):
        keys=list()
        visited=set()
        if len(rooms)==0:
            return True
        keys.extend(rooms[0])
        visited.add(0)

        while len(keys)>0:
            key=keys[0]
            del keys[0]
            if key not in visited:
                visited.add(key)
                keys.extend(rooms[key])

        return True if len(rooms)==len(visited) else False
            






                

        
        
if __name__=="__main__":
    c=Solution()
    print(c.canVisitAllRooms2([[1],[2],[3],[]])) #True
    print(c.canVisitAllRooms2([[1,3],[3,0,1],[2],[0]])) #False
    print(c.canVisitAllRooms2([[2],[],[1]])) #True

        