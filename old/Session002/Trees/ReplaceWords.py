class Solution:
    """
    https://leetcode.com/problems/replace-words/

    Implemented using Trie data structure
    """

    def replaceWords(self, dict: 'List[str]', sentence: str) -> str:
        self.root=self.TrieNode()
        for item in dict:
            self._insert(item)
        res=[]
        splt=sentence.split(' ')
        for word in splt:
            res.append(self._search(word))
        return ' '.join(res)


    def _insert(self, key:str):
        cur=self.root
        for c in key:
            next=None
            if c not in cur.children:
                next=self.TrieNode()
                cur.children[c]=next
            else:
                next=cur.children[c]
            cur=next
        cur.is_word=True
        cur.val=key
    
    def _search(self, key):
        cur=self.root
        for c in key:
            if c not in cur.children:
                if cur.is_word:
                    return cur.val
                else:
                    return key
            else:
                if cur.is_word:
                    return cur.val
                cur=cur.children[c]
        return key



    class TrieNode:
        def __init__(self):
            self.children={}
            self.is_word=False
            self.val=None
if __name__ == "__main__":
    c=Solution()
    print(c.replaceWords(["cat", "bat", "rat"], "the cattle was rattled by the battery"))#"the cat was rat by the bat"
    print(c.replaceWords(["a", "aa", "aaa", "aaaa"], "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"))#"a a a a a a a a bbb baba a"