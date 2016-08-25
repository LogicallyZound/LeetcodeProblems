class Solution(object):

    def longestConsecutive(self, nums):

        """

        :type nums: List[int]

        :rtype: int

        """

        d = {}

        if len(nums) <= 1:

            return len(nums)

        

        for n in nums:

            l = d.get(n-1, 0)

            r = d.get(n+1, 0)

            val  = l + r + 1

            

            if n not in d:

                d[n] = val

                if l != 0:

                    d[n-l] = val

                if r != 0:

                    d[n+r] = val

        mx = max(d, key = d.get)

        return d[mx]
