class Solution(object):

    def reverseWords(self, s):

        """

        :type s: str

        :rtype: str

        """

        

        

            

        ls = s[::-1].split()

        res = []

        for l in ls:

            res.append(l[::-1])

        return ' '.join(res)

        

        
