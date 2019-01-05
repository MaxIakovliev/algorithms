class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        available=set(wordList)
        processed=[]
        processed.append(beginWord)
        distance=1
        while endWord not in processed:
            toAdd=set()
            for item in processed:
                for i in range(len(item)):
                    for ch in range(ord('a'),ord('z')+1):
                    
                        newItem=item[:i]+chr(ch)+item[i+1:]
                        if newItem in available:
                            toAdd.add(newItem)
                            available.remove(newItem)
            distance+=1
            if len(toAdd)==0:
                return 0
            processed=toAdd
        return distance

    def ladderLength2(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        available=set(wordList)
        processed=set()
        processed.add(beginWord)
        count=1
        while endWord not in processed:
            curAdd=set()
            for item in  processed:
                for i in range(len(item)):
                    for j in range(ord('a'), ord('z')+1):
                        newWord=item[:i]+chr(j)+item[i+1:]
                        if newWord in available:
                            curAdd.add(newWord)
                            available.remove(newWord)
            count+=1
            if len(curAdd)==0:
                return 0
            processed=curAdd
        return count



    def ladderLength3(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        available=set(wordList)
        processed=set()
        processed.add(beginWord)
        count=1
        while endWord not in processed:
            curAdd=set()
            for item in processed:
                for i in range(len(item)):
                    for ch in range(ord('a'), ord('z')+1):
                        newWord=item[:i]+chr(ch)+item[i+1:]
                        if newWord in available:
                            curAdd.add(newWord)
                            available.remove(newWord)
            count+=1
            if len(curAdd)==0:
                return 0
            processed=curAdd
        return count
                        



 


if __name__=="__main__":
    c=Solution()
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    print(c.ladderLength2(beginWord,endWord,wordList))
