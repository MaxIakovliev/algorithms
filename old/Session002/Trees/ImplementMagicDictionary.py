class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root=self.TrieNode()
        

    def buildDict(self, dict: 'List[str]') -> None:
        """
        Build a dictionary through a list of words
        """
        for item in dict:
            self._insert(item)
        

    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        #if self._search(word):
        #    return False

        for i in range(len(word)):
            for c in range(ord('a'), ord('z')+1):
                new_word=word[:i]+chr(c)+word[i+1:]
                if new_word==word:
                    continue
                if self._search(new_word):
                    return True
        return False

    def _search(self, word):
        cur=self.root
        for c in word:
            if c not in cur.children:
                return False
            else:
                cur=cur.children[c]
        if cur.is_word and cur.val==word:
            return True
        else:
            return False
    
    def _insert(self, word):
        cur=self.root
        for c in word:
            next=None
            if c not in cur.children:
                next=self.TrieNode()
                cur.children[c]=next
            else:
                next=cur.children[c]
            cur=next
        cur.is_word=True
        cur.val=word



    class TrieNode:
        def __init__(self):
            self.children={}
            self.is_word=False
            self.val=None

if __name__ == "__main__":
    c=MagicDictionary()
    c.buildDict(["hello", "leetcode"])
    print(c.search("hello"))#false
    print(c.search("hhllo"))#true
    print(c.search("hell"))#false
    print(c.search("leetcoded"))#false
    print(c.search("leetcoda"))#true


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)