class Solution:
    def floodFill(self, image: 'List[List[int]]', sr: int, sc: int, newColor: int) -> 'List[List[int]]':
        color=image[sr][sc]
        tofill=[]
        tofill.append((sr,sc))
        while len(tofill)>0:
            cord=tofill.pop()
            image[cord[0]][cord[1]]=newColor
            if cord[0]+1<len(image) and image[cord[0]+1][cord[1]]==color and image[cord[0]+1][cord[1]]!=newColor:
                tofill.append((cord[0]+1,cord[1]))
            if cord[0]<len(image) and cord[1]+1<len(image[cord[0]]) and  image[cord[0]][cord[1]+1]==color and image[cord[0]][cord[1]+1]!=newColor:
                tofill.append((cord[0],cord[1]+1))
            if cord[0]-1>=0 and image[cord[0]-1][cord[1]]==color and image[cord[0]-1][cord[1]]!=newColor:
                tofill.append((cord[0]-1,cord[1]))
            if cord[0]>=0  and cord[1]-1>=0 and  image[cord[0]][cord[1]-1]==color and image[cord[0]][cord[1]-1]!=newColor:
                tofill.append((cord[0],cord[1]-1))
        return image

if __name__ == "__main__":
    c=Solution()
    print(c.floodFill([[1,1,1],[1,1,0],[1,0,1]],1,1,2))
    print(c.floodFill([[0,0,0],[0,1,1]],1,1,1))