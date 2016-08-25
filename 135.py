
class Solution(object):

    def candy(self, ratings):

        """

        :type ratings: List[int]

        :rtype: int

        """

        

        if len(ratings) <= 1:

            return len(ratings)

            

            

        candies = [1]*len(ratings)

        

        for i in range(1, len(ratings)):

            if ratings[i-1] < ratings[i]:

                candies[i] = candies[i-1]+1

        for j in range(len(ratings)-2, -1, -1):

            if ratings[j] > ratings[j+1]:

                candies[j] = max(candies[j], candies[j+1]+1)

        

                

        return sum(candies)











