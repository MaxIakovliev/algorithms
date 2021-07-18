class Solution:
    """
    https://leetcode.com/problems/reveal-cards-in-increasing-order/
    answer: https://leetcode.com/problems/reveal-cards-in-increasing-order/discuss/257891/Python-(easy-to-understand)-solution
    """
    def deckRevealedIncreasing(self, deck: 'List[int]') -> 'List[int]':
        sd= sorted(deck, reverse=True)
        order=[]
        while len(sd)>0:
            order.insert(0,sd[0])
            i=order[-1]
            order.insert(1,i)
            order.pop()
            sd.pop(0)
        return order

        