class Solution(object):

    def trap(self, height):

        """

        :type height: List[int]

        :rtype: int

        """

        

        arr = [0] * len(height)

        highest = 0

        res = [0]*len(height)

        for i in range(len(height)):

            highest = max(highest, height[i])

            arr[i] = max (highest, height[i])

        highest = 0

        for i in range(len(height)-1, -1, -1):

            highest = max(highest, height[i])

            arr[i] = min(highest, arr[i])

        for a in range(len(arr)):

            res[a] = arr[a] - height[a]

        return sum(res)
