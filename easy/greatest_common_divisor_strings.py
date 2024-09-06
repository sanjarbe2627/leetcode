# 1071. Greatest Common Divisor of Strings
# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).
# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        print("----->", str1, str2)

        if len(str2) > len(str1):
            str1, str2 = str2, str1

        if str2 == str1:
            return str1

        if str1[:len(str2)] != str2:
            return ""

        return self.gcdOfStrings(str1[len(str2):], str2)


data = Solution()
print(data.gcdOfStrings(str1="ABABAB", str2="ABAB"))
