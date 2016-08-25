class Solution(object):

    def maxProfit(self, prices):

        """

        :type prices: List[int]

        :rtype: int

        """

        if len(prices) <= 1:

            return 0

        if len(prices) == 2:

            return 0 if prices[1] <= prices[0] else prices[1]- prices[0]

        

        

        one = [0]*len(prices)

        two = [0]*len(prices)

        mn = prices[0]

        

        for i in range(1, len(prices)):

            mn = min(mn, prices[i])

            one[i]= max (one[i-1], prices[i] - mn)

            

        mx = prices[len(prices)-1]

        for i in range(len(prices)-2, -1, -1):

            mx = max(mx, prices[i])

            two[i] = max(two[i+1], mx-prices[i])

        

        res  = 0

        for i in range(len(prices)):

            res = max(res, one[i] + two[i])

       # print one, two

        return res

        
