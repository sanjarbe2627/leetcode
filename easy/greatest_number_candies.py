# 1431. Kids With the Greatest Number of Candies
# There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.
# Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        result = []

        max_candies = candies[0]
        for candy in candies:
            max_candies = candy if candy >= max_candies else max_candies

        for candy in candies:
            result.append(candy + extraCandies >= max_candies)

        return result

data = Solution()
print(data.kidsWithCandies([2,3,5,1,3], 3))