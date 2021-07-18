class Solution:
    """
    https://leetcode.com/problems/escape-the-ghosts/
    our distance to target is abs(t[0]) + abs(t[1]).
    For every ghost g, distance to target is abs(t[0] - g[0]) + abs(t[1] - g[1]).
    You need to be closer to target than any ghost to escape.
    """
    def escapeGhosts(self, ghosts: 'List[List[int]]', target: 'List[int]') -> bool:
        dist=abs(target[0])+abs(target[1])
        for item in ghosts:
            if dist>=abs(target[0]-item[0])+abs(target[1]-item[1]):
                return False
        return True

        