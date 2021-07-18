class Solution(object):
    """
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
    """

    def maxProfit(self, a):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(a) == 0:
            return 0
        minVal = a[0]
        summary = 0
        curMax = 0
        for i in range(1, len(a)):
            if a[i] > minVal and a[i] > a[i-1]:
                curMax = max(curMax, a[i]-minVal)
            else:
                summary += curMax
                curMax = 0
                minVal = a[i]
        summary += curMax
        return summary

    def maxProfit2(self, a):
        """
        :type prices: List[int]
        :rtype: int
        """
        t1 = 0
        t2 = float("-inf")
        for price in a:
            t1_prev = t1
            t1 = max(t1, t2+price)
            t2 = max(t2, t1_prev-price)
        return t1


if __name__ == "__main__":
    c = Solution()
    print(c.maxProfit2([7, 1, 5, 3, 6, 4]))  # 7
    print(c.maxProfit2([1, 2, 3, 4, 5]))  # 4
    print(c.maxProfit2([7, 6, 4, 3, 1]))  # 0
    print(c.maxProfit2([6, 1, 3, 2, 4, 7]))  # 7
