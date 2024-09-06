# 151. Reverse Words in a String
# Given an input string s, reverse the order of the words.
# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
# Return a string of the words in reverse order concatenated by a single space.
# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.
class Solution(object):
    def reverseWords(self, s):
        s = s.split()
        result = ''
        for i in range(len(s) - 1,  -1, -1):
            if s[i]:
                result += s[i]
                if i != 0:
                    result += " "
        return result

data = Solution()
print(data.reverseWords("  hello world  "))